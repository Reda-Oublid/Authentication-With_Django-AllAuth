const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')
const gridContainer = document.getElementById('grid-container')

/**
 * Toggles the sidebar's visibility, rotates the toggle button, and adjusts the grid container's layout.
 *
 * @function toggleSidebar
 * @returns {void}
 */
function toggleSidebar(){

  sidebar.classList.toggle('close')
  toggleButton.classList.toggle('rotate')
  gridContainer.classList.toggle('grid-container-collapsed-sidebar')

  closeAllSubMenus()
}

/**
 * Toggles the visibility of a submenu and rotates the corresponding icon.
 * If the submenu is not visible, all other submenus are closed.
 * If the sidebar is in a closed state, it is opened and the toggle button is rotated.
 *
 * @function toggleSubMenu
 * @param {HTMLElement} button - The button that triggers the submenu toggle.
 * @returns {void}
 */
function toggleSubMenu(button){

  if(!button.nextElementSibling.classList.contains('show')){
    closeAllSubMenus()
  }

  button.nextElementSibling.classList.toggle('show')
  button.classList.toggle('rotate')


  if(sidebar.classList.contains('close')){
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')
  }
}
/*
* close all subMenus
* use cases :
*   when the sidebar is closed
*   for responsive design
* */
function closeAllSubMenus(){
  Array.from(sidebar.getElementsByClassName('show')).forEach(ul => {
    ul.classList.remove('show')
    ul.previousElementSibling.classList.remove('rotate')
  })
}