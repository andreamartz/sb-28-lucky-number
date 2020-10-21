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

/** handleResponse: deal with response from our lucky-num API. */
function handleResponse(res) {
  // empty page of prior responses and error messages
  nameErr.innerText = '';
  yearErr.innerText = '';
  emailErr.innerText = '';
  colorErr.innerText = '';
  results.innerHTML = '';

  let res_errors = res["data"]["errors"]

  if (res_errors) {
    if (res_errors["name"]) {
      nameErr.innerText = res_errors["name"][0];
    }
    if (res_errors["year"]) {
      yearErr.innerText = res_errors["year"][0];
    }
    if (res_errors["email"]) {
      emailErr.innerText = res_errors["email"][0];
    }
    if (res_errors["color"]) {
      colorErr.innerText = res_errors["color"][0];
    }
  } else {
    results.innerHTML = `<p>Your lucky number is ${res["data"]["num"]["num"]} (${res["data"]["num"]["fact"]}).</p><p>Your birth year (${res["data"]["year"]["year"]}) fact is ${res["data"]["year"]["fact"]}</p>`;
    form.reset();
  }
}

form.addEventListener("submit", async function(evt) {
  res = await processForm(evt); // response from Flask backend API
  handleResponse(res);
})
