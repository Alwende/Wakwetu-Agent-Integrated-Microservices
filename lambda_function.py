import json
def lambda_handler(event, context):
    action_group = event.get("actionGroup")
    function = event.get("function")
    if function == "get_account_balance":
        response_body = {"account_id": "WAK-789", "balance": 5250.75, "currency": "USD"}
    else:
        response_body = {"error": "Function not recognized"}
    return {
        "actionGroup": action_group,
        "function": function,
        "functionResponse": {
            "responseBody": {
                "TEXT": {"body": json.dumps(response_body)}
            }
        }
    }
