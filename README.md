# containerbox

Use a Docker host to execute requested code in containers

---

## Warning

This app is meant to be run on a throwaway machine, VPS, or hardware-based VM. I am not responsible for any damage, data exposure or loss caused by Docker vulnerability exploits if this app is chosen to be run in a real and mission-critical PC.

## Motivation

This is meant to be used with `pcp`, but feel free to use it for any other purposes.

## Endpoints

1. [ ] POST /  
   Request body:
   ```json
   {
     "lang": "string",
     "code": "string"
   }
   ```
   Response body:
   ```json
   {
     "status": number,
     "stdout": "string"
   }
   ```
