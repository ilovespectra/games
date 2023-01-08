
1 Have Node.js installed in your system.

2 In CMD, run the command ```npm install http-server -g```

3 Navigate to the specific path of your file folder in CMD and run the command ```http-server```

4 Go to your browser and type ```localhost:8080``` Your Application should run there.

<h2> Optimist Calculator! </h2>
The Optmist Calculator is legit! It's super easy to modify the script to include any other tokens, you just need to add the following to their corresponding sections:

```
<br>
      <label>
        YOUR-TOKEN-HERE:
        <input type="number" id="YOUR-TOKEN-HEREquantity" value="0" min="0" step="0.00001">
      </label>
```
```
const YOUR-TOKEN-HEREAllTimeHigh = YOUR-TOKEN'S-ATH-HERE;
```
```
const YOUR-TOKEN-HEREQuantity = Number(document.querySelector('#YOUR-TOKEN-HEREquantity').value);
```
```
+ YOUR-TOKEN-HEREQuantity * YOUR-TOKEN-HEREAllTimeHigh
```
