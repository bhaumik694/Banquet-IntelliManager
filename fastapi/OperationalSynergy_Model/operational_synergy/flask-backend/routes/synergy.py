from flask import Blueprint, jsonify
from models.db import events_collection, menu_items_collection, events_collection
from services.synergy_engine import compute_synergy
from services.genai_service import generate_ai_insights

from bson import ObjectId
from dateutil import parser

synergy_bp = Blueprint("synergy", __name__)


# 🛡 SAFE AI
def safe_ai(metrics, event_name):
    try:
        return generate_ai_insights(metrics, event_name)
    except Exception as e:
        print("AI FAILED:", e)
        return "AI insights unavailable"


# 🔹 HEALTH CHECK
@synergy_bp.route("/", methods=["GET"])
def health():
    return jsonify({"message": "Synergy API running 🚀"})


# 🔍 DEBUG ROUTE
@synergy_bp.route("/debug", methods=["GET"])
def debug():
    events = list(events_collection.find())
    return jsonify({
        "count": len(events),
        "ids": [str(e["_id"]) for e in events]
    })


# 🔧 HELPER FUNCTION
def parse_datetime(value):
    try:
        return parser.parse(value) if isinstance(value, str) else value
    except Exception as e:
        print("DATE PARSE ERROR:", e)
        return None


# 🔥 FETCH MENU FOR EVENT (IMPORTANT)
def get_event_menu(event_id):

    menu_doc = events_collection.find_one({
        "$or": [
            {"event": event_id},
            {"event": str(event_id)}
        ]
    })

    if not menu_doc:
        print("⚠️ No menu found for event:", event_id)
        return []

    item_ids = []

    # flatten all categories
    for category in menu_doc.get("selections", {}).values():
        for item in category:
            item_ids.append(item)

    if not item_ids:
        return []

    # fetch actual menu items
    items = list(menu_items_collection.find({
        "_id": {"$in": item_ids}
    }))

    return items


# 🚀 MAIN ROUTE
@synergy_bp.route("/<event_id>", methods=["GET"])
def get_synergy(event_id):

    # 🔍 Find event
    try:
        current_event = events_collection.find_one({"_id": ObjectId(event_id)})
    except:
        current_event = events_collection.find_one({"_id": event_id})

    if not current_event:
        return jsonify({"error": "Event not found"}), 404

    print("\n🔥 CURRENT EVENT:", current_event.get("partyName"))

    all_events = list(events_collection.find())
    results = []

    current_end = parse_datetime(
        current_event.get("schedule", {}).get("endDateTime")
    )

    # 🔥 FETCH CURRENT MENU
    current_items = get_event_menu(current_event["_id"])

    for event in all_events:

        if str(event["_id"]) == str(current_event["_id"]):
            continue

        start = parse_datetime(
            event.get("schedule", {}).get("startDateTime")
        )

        if not start or not current_end:
            continue

        try:
            gap = abs((start - current_end).total_seconds()) / 3600
        except Exception as e:
            print("❌ GAP ERROR:", e)
            continue

        if gap > 48:
            continue

        # 🔥 FETCH ADJACENT MENU
        adj_items = get_event_menu(event["_id"])

        # ❗ skip if no menu
        if not current_items or not adj_items:
            print("⚠️ Skipping due to empty menu")
            continue

        try:
            synergy = compute_synergy(current_items, adj_items, gap)
        except Exception as e:
            print("❌ SYNERGY ERROR:", e)
            continue

        ai_text = safe_ai(
            synergy.get("metrics", {}),
            event.get("partyName", "Event")
        )

        results.append({
            "eventId": str(event["_id"]),
            "eventName": event.get("partyName", "Unknown"),
            **synergy,
            "aiInsights": ai_text
        })

    # 🧨 FALLBACK
    if not results:
        fallback_metrics = {
            "cuisineOverlapPct": 0,
            "heavyPrepItems": 0,
            "commonCategories": 0,
            "timeGapHours": 0,
            "efficiencyGain": 10
        }

        results.append({
            "eventId": None,
            "eventName": "No Adjacent Events",
            "metrics": fallback_metrics,
            "efficiencyGain": 10,
            "aiInsights": safe_ai(
                fallback_metrics,
                current_event.get("partyName", "Event")
            )
        })

    return jsonify({
        "data": results,
        "aiEnabled": True
    })