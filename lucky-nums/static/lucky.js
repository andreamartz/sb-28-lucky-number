// const BASE_URL = "http://127.0.0.1:5000/api/get_lucky_num";
// const BASE_URL = "http://localhost:5000/api/get_lucky_num";
const BASE_URL = "/api/get-lucky-num";

const results = document.querySelector('#lucky-results');
const form = document.querySelector('#lucky-form');
let nameErr = document.querySelector("#name-err");
let yearErr = document.querySelector("#year-err");
let emailErr = document.querySelector("#email-err");
let colorErr = document.querySelector("#color-err");

/** processForm: get data from form and make AJAX call to our API. */

// GIVEN:
// function processForm(evt) {
// }

async function processForm(evt) {
  evt.preventDefault();
  // get data from form
  const name = document.querySelector("#name").value;
  const year = document.querySelector("#year").value;
  const email = document.querySelector("#email").value;
  const color = document.querySelector("#color").value;
  console.log("form values: ", name, year, email, color);

  const formData = {name, year, email, color};
  // const formData = {"name": name, "year": year, "email": email, "color": color};
  // const formData = {name: name, year: year, email: email, color: color};
  console.log("formData: ", formData);

  // make AJAX call to our Flask API
  const res = await axios.post(`${BASE_URL}`, formData);

  console.log("post request result: ", res);

  return res;
}

form.addEventListener("submit", async function(evt) {
  res = await processForm(evt); // response from Flask backend API
  handleResponse(res);
})


// GIVEN:
// function handleResponse(resp) {
// }


/** handleResponse: deal with response from our lucky-num API. */
function handleResponse(res) {
  if (res["errors"]) {
    nameErr.innerText = res["errors"]["name"][0] || '';
    console.log("I looked at 'name'!");
    yearErr.innerText = res["errors"]["year"][0] || '';
    emailErr.innerText = res["errors"]["email"][0] || '';
    colorErr.innerText = res["errors"]["color"][0] || '';
  }
    // if (res["errors"]["name"]) {
  //   nameErr.innerText = res["errors"]["name"][0];
  // }

  // if (res["errors"]["year"]) {
  //   yearErr.innerText = res["errors"]["year"][0];
  // }

  // if (res["errors"]["email"]) {
  //   emailErr.innerText = res["errors"]["email"][0];
  // }

  // if (res["errors"]["color"]) {
  //   colorErr.innerText = res["errors"]["color"][0];
  // }
  console.log("LINE 75 res: ", res);
  if (!res["errors"]) {
    results.innerHTML = `<p>Your lucky number is ${res["data"]["num"]["num"]} (${res["data"]["num"]["fact"]}).</p><p>Your birth year (${res["data"]["year"]["year"]}) fact is ${res["data"]["year"]["fact"]}</p>`
  }
}
// how to get the result variable out?
// GIVEN:
// $("#lucky-form").on("submit", processForm);
