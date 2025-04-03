import json
from datetime import datetime, timedelta, timezone

input_file_path = "temp/input/chainoffers_data.json"
output_file_path = "src/profile/chain_offers.json"

try:
    with open(input_file_path, "r") as data_file:
        data = json.load(data_file)

    offers = data.get("offers", [])

    offerList = []
    index = 0

    for offer in offers:
        cost = offer.get("cost", 0)
        rewards = offer.get("rewards", {})
        cooldown = offer.get("cooldown", 0)
        if rewards:
            offer_data = {
                "index": index,
                "cost": cost,
                "productId": None,
                "fallbackProductId": None,
                "cooldown": cooldown,
                "claimed": True,
                "rewards": rewards,
                "colorSchema": None,
            }
        else:
            productId = offer.get("productId", None)
            fallbackProductId = offer.get("fallbackProductId", None)
            colorSchema = offer.get("colorSchema", None)
            offer_data = {
                "index": index,
                "productId": productId,
                "fallbackProductId": fallbackProductId,
                "cooldown": cooldown,
                "claimed": True,
                "colorSchema": colorSchema,
            }

        offerList.append(offer_data)
        index += 1

    chainOffers = {
        "chain_offers_promo": {
            "id": "chain_offers_promo",
            "timeSlotId": data.get("timeSlot", ""),
            "homeButton": data.get("homeButton", {}),
            "offers": offerList,
            "fallBackProductId": "chili_coins_pack_2",
            "fallBackReward": data.get("fallbackReward", {}),
        }
    }

    final_data = {
        "lastSaved": "1970-01-01T00:00:00Z",
        "chainOffers": chainOffers,
        "completedChainOffers": [],
    }

    output_data = {"version": 1, "data": final_data}

    with open(output_file_path, "w") as f:
        json.dump(output_data, f, indent=2)

except IOError as e:
    print(f"Error opening or accessing chainoffers_data.json: {e}")
