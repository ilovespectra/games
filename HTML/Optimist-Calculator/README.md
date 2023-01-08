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
