# Cloud Engineering Quiz

A serverless quiz web app with a shared class scoreboard, built on AWS. Each attempt is a 50-question exam drawn at random from a larger question bank, and students get a personal cheat sheet of the topics they missed.

Built as part of my cloud engineering studies. Full write-up: _add your Medium link here_.

## Features

- 50 questions per attempt, drawn at random with a fixed difficulty mix (easy, medium, hard)
- Two modes: random order, or easy to hard
- Instant feedback with a short explanation after every answer
- Personal cheat sheet of missed topics, printable or saveable as PDF
- Shared class scoreboard stored in DynamoDB (best score and attempts per player)
- Local score history in the browser as a fallback

## Architecture

```
Browser
  |  loads the page
  v
Amazon S3 (static website: index.html)
  |  fetch()
  v
Amazon API Gateway (HTTP API)
  |-- POST /results --> Lambda: quiz-save-result --> DynamoDB: quiz-results
  |-- GET  /scores  --> Lambda: quiz-get-scores  --> DynamoDB: quiz-results
```

| Service | Role |
| --- | --- |
| S3 | Hosts the single-file front end as a static website |
| API Gateway (HTTP API) | Public front door with two routes |
| Lambda (Python) | `quiz-save-result` validates and stores a result, `quiz-get-scores` returns the top scores |
| DynamoDB (on-demand) | Stores results, so there is no hourly cost |

## Repository structure

```
frontend/index.html                    The whole quiz page (HTML, CSS, JS)
backend/lambda/save_result.py          Saves one result
backend/lambda/get_scores.py           Returns the top ten players
backend/lambda/test-events.md          Test events for both functions
infra/lambda-dynamodb-policy.json      Least-privilege IAM policy for the Lambda roles
infra/s3-bucket-policy.json            Public-read policy for the website bucket
infra/cors.md                          API Gateway CORS settings
```

## Setup

Use region `us-east-1` for everything, or adjust the policies to your region.

1. **DynamoDB:** create a table named `quiz-results` with partition key `quizId` (String) and sort key `submittedAt` (String). Set capacity mode to **On-demand**.
2. **Lambda:** create two Python functions, `quiz-save-result` (paste `save_result.py`) and `quiz-get-scores` (paste `get_scores.py`). Deploy both.
3. **IAM:** on each function's execution role, add an inline policy from `infra/lambda-dynamodb-policy.json`, replacing `YOUR-ACCOUNT-ID`.
4. **Test:** run the events in `backend/lambda/test-events.md`. Check the response body and the table, not just the status code.
5. **API Gateway:** create an **HTTP API** named `quiz-api` with routes `POST /results` to `quiz-save-result` and `GET /scores` to `quiz-get-scores`. Keep the `$default` stage with auto-deploy.
6. **CORS:** configure it as described in `infra/cors.md`.
7. **Front end:** open `frontend/index.html` and replace the `API` constant near the top of the script with your API's invoke URL.
8. **S3:** create a bucket, upload the file named exactly `index.html`, enable **Static website hosting** (index document `index.html`), turn off Block Public Access, and apply `infra/s3-bucket-policy.json` with your bucket name.

Open the website endpoint and take an exam. The result screen should say the score was saved, and the class scoreboard should list the player.

## Troubleshooting

| Problem | Likely cause |
| --- | --- |
| 403 on the website | Bucket is still private, or the bucket policy is missing |
| 404 on the website | File is not named `index.html`, or is inside a folder |
| Scoreboard says unavailable, or scores do not save | CORS: missing origin, or `content-type` is not under Allow-Headers |
| Save test returns an empty list | Read function code was pasted into the save function |
| Old version still showing | Hard refresh with Ctrl+Shift+R |

## Cost

Everything is serverless and pay-per-use. A class-sized quiz sits within the AWS free tiers for Lambda, API Gateway and DynamoDB, and S3 hosting costs a few cents a month. Set a billing alert anyway.

## Known limitations

- No authentication, so anyone who finds the API address could post a fake score. The Lambda validates input, which limits the damage.
- S3 website endpoints are HTTP only. Put CloudFront in front for HTTPS.
- The question bank is static, built from verified fact lists inside the page.

## Roadmap

- CloudFront in front of S3 for HTTPS
- Cognito login so scores belong to verified users
- Move the question bank into DynamoDB
- Per-topic progress charts
- Infrastructure as code with CloudFormation or Terraform

## License

MIT, see `LICENSE`.
