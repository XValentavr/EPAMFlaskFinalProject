fetch("/api/employees")
    .then((response) => response.json())
    .then((data) => {
        DisplayGotData(data);
    })
    .catch((error) => console.log(error))

function DisplayGotData(data) {
    if (data.length === 0) {
        let empty = document.getElementById("empty");
        let text = document.createTextNode("No employees of hospital were found");
        empty.appendChild(text);
    } else {
        CreateTable(GetData(data));
    }
}

function GetData(data) {
    let information = []
    for (let i = 0; i < data.length; i++) {
        let current_employees = data[i];
        if (current_employees['hospital_id'] === null) {
            current_employees['hospital_id'] = 'Not specified'
        }
        let json_employee = {
            'identifier': current_employees['id'],
            'Name': current_employees['name'],
            'Date of birth': current_employees['date_of_birth'],
            'Salary': current_employees['salary'],
            'Department': current_employees['hospital_id']
        }
        information.push(json_employee)
    }
    return information
}

function CreateTable(data) {
    let session = document.getElementById("session").textContent
    let table = document.querySelector("table");
    let keys = Object.keys(data[0])
    for (let i = 0; i < data.length; i++) {
        let element = data[i];
        let row = table.insertRow();
        for (let j = 1; j < keys.length; j++) {
            let cell = row.insertCell();
            let text = document.createTextNode(element[keys[j]]);
            cell.appendChild(text);
        }
        if (session.includes('True')) {
            //create edit link
            let cell = row.insertCell();
            let a = document.createElement("a");
            a.setAttribute("href", `/employees/edit/${element['identifier']}`);
            let text = document.createTextNode("Edit");
            a.appendChild(text);
            cell.appendChild(a);
            cell = row.insertCell();
            //create delete request
            a = document.createElement("a");
            a.setAttribute("onclick", `api_delete_employee(${element['identifier']})`)
            text = document.createTextNode("Delete");
            a.appendChild(text);
            cell.appendChild(a);
        }
    }
}

function api_delete_employee(identifier) {
    fetch(`/api/employees/${identifier}`, {
        method: 'DELETE'
    })
        .then((response) => response.json())
        .then(() => {
            window.location.href = `/employees`;
        })
        .catch(() => {
            swal("An error occured. Please check insert data.")
                .then(() => {
                    window.location = document.URL;
                });
        })
}