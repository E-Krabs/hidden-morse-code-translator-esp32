# hidden-morse-code-translator-esp32

Translates morse from buttons under toes and vibrates target language's result via Google Translate.<br>
<h3>Usage</h3>
<p>Input:<br>
Uses two buttons placed under the big toes. Use the left button (key) to input either a dot or a dash. Use the right button (ctrl) to input a 1 space between letters, or 2 spaces between words. Holding down the control key submits the query for translation. Holding it down longer clears the input.</p>
<p>Output:<br>
After sending the encoded word in the source language to the API for translation, the target language translation will be re-encoded back into morse and vibrate on the user's leg or foot for interpretation.</p>

<h3>Parts</h3>
<ul>
  <li>Any esp32 with micropython (https://www.amazon.com/HiLetgo-ESP-32S-Bluetooth-Wireless-ESP-WROOM-32/dp/B077KJNVFP/)</li>
  <li>2x Buttons (<href src="https://www.aliexpress.us/item/3256801735655471.html?spm=a2g0o.productlist.main.5.6dc118edIIAnYi&algo_pvid=07669b71-7154-402e-83de-f07114f854c0&algo_exp_id=07669b71-7154-402e-83de-f07114f854c0-2&pdp_npi=3%2540dis!USD!1.80!1.62!!!1.80!!">https://www.aliexpress.us/item/3256801735655471.html</href>)</li>
  <li>LiPo 3.7V 1500mAh Battery (www.amazon.com/EEMB-Battery-Rechargeable-Connector-Certified/dp/B09DPMS6HN)</li>
  <li>Vibration Motor (www.amazon.com/DZS-Elec-Button-type-Electronics-Appliances/dp/B07PHRX7QH)</li>
</ul>
