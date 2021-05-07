function deleteContact(conId) {
    fetch('/delete_contact', {
        method: 'POST',
        body: JSON.stringify({ phoneId: conId })
    }).then((_res) => {
        window.location.href = "/";
    });
}