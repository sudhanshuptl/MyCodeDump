# Enable auto refresh web server on making change
* initilize `npm init`
* install package `npm install nodemon`
* Update the script in `package.json`. here `app.js` is main file.
```
 "scripts": {
    "dev": "nodemon app.js"
  },
```
* `npm run dev` to execute in auto refresh mode

# Install
* Other dependecies:  `npm i express`