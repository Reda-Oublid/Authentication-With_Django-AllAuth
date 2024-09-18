function showEditForm() {
    document.getElementById('description-view').style.display = 'none';
    document.getElementById('description-edit').style.display = 'block';
  }

  function cancelEdit() {
    document.getElementById('description-view').style.display = 'flex';
    document.getElementById('description-edit').style.display = 'none';
  }