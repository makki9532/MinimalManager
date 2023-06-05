// api.js

const API_URL = 'http://127.0.0.1:8000/api';
const token = localStorage.getItem("token");

export async function getItem(endpoint) {
  try {
    const res = await fetch(`${API_URL}/${endpoint}/`, {
      method: 'GET',
      headers: {
        'Authorization': `Token ${token}`
      },
      credentials: "include",
      mode: "cors",
      referrerPolicy: "no-referrer",
    });
    const data = await res.json();
    return data;
  } catch (error) {
    const status = {"error" : true}
    return status
  } 
}

export async function postItem(request_body, endpoint) {
  const res = await fetch(`${API_URL}/${endpoint}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    },
    body: JSON.stringify(request_body),
    credentials: "include",
    mode: "cors",
    referrerPolicy: "no-referrer",
  });
  const data = await res.json();
  return data;
}

export async function delItem(id, endpoint) {
  const res = await fetch(`${API_URL}/${endpoint}/${id}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    },
    credentials: "include",
    mode: "cors",
    referrerPolicy: "no-referrer",
  });
  return res
}

export async function putItem(id, request_body, endpoint) {
  const res = await fetch(`${API_URL}/${endpoint}/${id}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    },
    body: JSON.stringify(request_body),
    credentials: "include",
    mode: "cors",
    referrerPolicy: "no-referrer",
  });
  const data = await res.json();
  return data;
}


