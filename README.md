# Discord-Emojis

Flatten the list of Discord Emojis. The `emojis.json` file should be replaced with:
- inspect element 
- go to the "sources" tab
- find `assets/bd028ce6ab8036567bcb.js`
- 32nd search result of `function(e){e.exports=JSON.parse` (starts similarly with provided `emojis.json`)
- save that JSON as `emojis.json` in this directory
