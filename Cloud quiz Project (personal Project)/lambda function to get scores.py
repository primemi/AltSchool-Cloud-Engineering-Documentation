import json, boto3
from boto3.dynamodb.conditions import Key

table = boto3.resource("dynamodb").Table("quiz-results")


def lambda_handler(event, context):
    items = []
    resp = table.query(KeyConditionExpression=Key("quizId").eq("cloud-quiz"))
    items += resp["Items"]
    while "LastEvaluatedKey" in resp:
        resp = table.query(
            KeyConditionExpression=Key("quizId").eq("cloud-quiz"),
            ExclusiveStartKey=resp["LastEvaluatedKey"],
        )
        items += resp["Items"]

    best = {}
    for it in items:
        name = it["name"]
        score = int(it["score"])
        if name not in best or score > best[name]["score"]:
            best[name] = {"name": name, "score": score, "total": int(it["total"]), "attempts": 0}
    for it in items:
        best[it["name"]]["attempts"] += 1

    top = sorted(best.values(), key=lambda r: -r["score"])[:10]
    return {"statusCode": 200, "body": json.dumps(top)}
