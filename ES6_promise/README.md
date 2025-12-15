# ES6 Promises

This project explores ES6 Promises in JavaScript, covering Promise creation, resolution, rejection, and advanced patterns.

## Learning Objectives

- Understand Promises (how, why, and what)
- Use `then`, `resolve`, `catch` methods
- Use every method of the Promise object
- Implement Throw / Try error handling
- Use the `await` operator
- Create and use async functions

## Requirements

- Ubuntu 20.04 LTS
- NodeJS 20.x.x
- npm 9.x.x
- All files end with a new line
- Code uses `.js` extension
- Code tested using Jest
- Code verified against ESLint

## Setup

Install dependencies:

```bash
npm install
```

## Tasks

0. **0-promise.js** - Return a Promise using getResponseFromAPI()
1. **1-promise.js** - Return a promise based on boolean parameter
2. **2-then.js** - Handle promise responses with then/catch/finally
3. **3-all.js** - Handle multiple successful promises
4. **4-user-promise.js** - Return a resolved promise with user object
5. **5-photo-reject.js** - Return a rejected promise
6. **6-final-user.js** - Handle multiple promises with allSettled
7. **7-load_balancer.js** - Return the fastest promise
8. **8-try.js** - Throw error for division by zero
9. **9-try.js** - Implement guardrail with try/catch

## Usage

Run tests:
```bash
npm test
```

Run dev:
```bash
npm run dev <filename>
```

Check linting:
```bash
npm run check-lint
```
