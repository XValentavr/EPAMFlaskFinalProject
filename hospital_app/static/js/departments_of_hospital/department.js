let identifier = document.URL.substring(document.URL.lastIndexOf('/') + 1);
if (document.title === "Edit department") {
    fetch(`/api/hospitals/${identifier}`)
        .then((response) => response.json())
        .catch(() => {
            window.location = '/hospitals';
        })
}

function checker_where_are_you() {
    if (document.title === "Edit department") {
        is_on_edit_department(get_data(), identifier)
    } else {
        is_on_add_department(get_data())
    }
}

function get_data() {
    let name = document.getElementById("Name of department").value;
    let to_do = document.getElementById('to_do').value
    let department = {
        'name': name,
        'to_do': to_do
    }
    return department
}

function is_on_edit_department(department, identifier) {
    fetch(`/api/hospitals/${identifier}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(department)
    })
        .then((response) => response.json())
        .then(() => {
            window.location = '/hospitals';
            alert('Its OK. I have changed a new department of hospital')
        })
        .catch(() => {
            window.location = document.URL;
            alert('An error occured. Please check insert data and try again')
        })
}

function is_on_add_department(department) {
    fetch(`/api/hospitals`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(department)
    })
        .then((response) => response.json())
        .then(() => {
            window.location = '/hospitals';
            alert('Its OK. I have added a new department of hospital')
        })
        .catch(() => {
            window.location = '/hospitals/add';
            alert('An error occured. Please check insert data and try again')
        })
}
