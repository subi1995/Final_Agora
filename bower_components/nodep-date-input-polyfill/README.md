# nodep-date-input-polyfill

Just include this simple script and IE, Firefox, and macOS Safari will support `<input type="date">`, without any dependencies, not even jQuery!

Support dynamically created inputs, so can be used in single page applications.

Forked from [html5-simple-date-input-polyfill](https://www.npmjs.com/package/html5-simple-date-input-polyfill). Continuing as a separate project.

## Demo

[Try it in IE, Firefox, and macOS Safari.](https://brianblakely.github.io/nodep-date-input-polyfill/)

## Install

### NPM

`npm install --save nodep-date-input-polyfill`

Add to your project:

* **Webpack / Rollup / Babel / ES:** `import 'nodep-date-input-polyfill';`

* **Webpack 1 / Browserify:** `require('nodep-date-input-polyfill');`

* **Script Tag:** Copy `nodep-date-input-polyfill.dist.js` from `node_modules` and
include it anywhere in your HTML.

* This package also supports **AMD**.

### Bower

`bower install nodep-date-input-polyfill`

## Features
* **Easily Stylable:** [These are the default styles](https://github.com/brianblakely/nodep-date-input-polyfill/blob/master/nodep-date-input-polyfill.scss),
which you may override with your own.

* **Polyfills `valueAsDate` and `valueAsNumber`:**
[Learn more about these properties.](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement#property-valueasdate)
They behave as getters and setters.

* **Keyboard Shortcuts:** `Esc` will hide the datepicker. `Up/Down` will
increment/decrement the date by one day.

* **Localization:** Specify the datepicker's locale by setting the
`lang` attribute of the `<input>` or any of its parent nodes.

    `<input type="date" lang="en" />`

    `<body lang="en">`

    The default locale is `en`.

    The rendered date format will automatically adhere to the given locale.

    Currently supported locales include:

    * English (US / UK)

    * Chinese (Simplified / Simplified Informal / Traditional)

    * Japanese

    * Spanish

    * Portuguese

    * Hindi

    * German

    * Dutch

    * Danish

    * Turkish

    * Ukrainian

    * French

    * Italian

    * Polish

    * Czech

    * Russian

## Usage Notes

* `getAttribute` and `setAttribute` will only reflect the field's text content.

* In order to work with the field's underlying value, you must get/set its
`value`, `valueAsDate`, or `valueAsNumber` properties.

* Per the native implementation, polyfilled date fields will only accept
values in the format `yyyy-MM-dd`.

* If a user dirties a date field by typing into it manually, the browser will no
longer allow the polyfill to populate the field from the datepicker.

    The polyfill will not attempt to solve this on its own.
    One potential workaround that you may choose to adopt
    is to prevent typing entirely:
    ```js
    el.addEventListener('keydown', (e)=> e.preventDefault());
    ```

* When submitting an HTML form, the browser will submit the date field's `value`
attribute (i.e. its text content), not the normalized content of the field's
`value` *property*.

    If you don't want that, one potential workaround is to change
    the attribute upon form submission:
    ```js
    el.form.addEventListener('submit', (e)=> el.setAttribute('value', el.value));
    ```

## Contributing

### Local Development
Run `npm start` or, for Cloud9 IDE users: `npm run start-c9`

### Build
Run `npm run build`

### Localization
Please submit PRs with new localizations! Open `locales.js` to add more.
File an issue on GitHub if anything is unclear.

## Thanks
Some words of appreciation for those who have submitted tickets, pull requests,
and new localizations.  The library is more robust and helpful to everyone
because of those who choose to help out.
