def generate_response(disaster):

    actions = {

        "Flood": [
            "Move to higher ground",
            "Avoid river areas",
            "Contact rescue services"
        ],

        "Wildfire": [
            "Leave forest area",
            "Wear protective mask",
            "Call fire department"
        ],

        "Cyclone": [
            "Stay indoors",
            "Avoid coastal areas",
            "Follow official alerts"
        ],

        "Drought": [
            "Conserve water",
            "Monitor water supplies",
            "Avoid unnecessary usage"
        ],

        "Landslide": [
            "Evacuate hilly areas",
            "Avoid steep slopes",
            "Contact emergency teams"
        ]
    }

    return {
        "disaster": disaster,
        "probability": "Predicted",
        "actions": actions.get(
            disaster,
            ["No Action Required"]
        )
    }