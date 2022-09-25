# http-client-parser
Parse and process http client files

## Installation
- Make sure you have `node`, `npm`, and `python` installed

## Instructions
### Set up sample server
- `cd sample-server && npm install`
- `npm run dev`
- This will bring up your local node-express server in port 8080
- It currently has only 1 API exposed for proof-of-concept

### Running the parser
- In a new terminal, run `python3 client-parser.py`
- This will call the sample endpoint after parsing the `sample-http-client.http`
- You can run, `python3 client-parser.py --dryrun` to just validate the http client file