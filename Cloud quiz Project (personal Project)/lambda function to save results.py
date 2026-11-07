import json, datetime, boto3

table = boto3.resource("dynamodb").Table("quiz-results")


def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body") or "{}")
        name = str(body.get("name", "")).strip()[:24]
        score = int(body.get("score"))
        total = int(body.get("total"))
        mode = str(body.get("mode", "random"))[:10]
        if not name or total != 50 or not 0 <= score <= total:
            return {"statusCode": 400, "body": json.dumps({"error": "invalid result"})}
        table.put_item(Item={
            "quizId": "cloud-quiz",
            "submittedAt": datetime.datetime.utcnow().isoformat(),
            "name": name,
            "score": score,
            "total": total,
            "mode": mode,
        })
        return {"statusCode": 200, "body": json.dumps({"saved": True})}
    except Exception:
        return {"statusCode": 400, "body": json.dumps({"error": "bad request"})}
