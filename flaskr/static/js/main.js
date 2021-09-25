const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const navLinks = document.querySelectorAll('.nav-links li');

  burger.addEventListener('click', () => {
    nav.classList.toggle('nav-active');

    navLinks.forEach((link, index) => {
      if(link.style.animation){
        link.style.animation = ''
      }else{
        link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + .5}s`;
      }
    });
    burger.classList.toggle('toggle');
  });

}
navSlide();

let currentScrollPosition = 0;
let scrollAmount = 320;
const sConst = document.querySelector(".hourly-container")
const hScroll = document.querySelector(".hourly-horizontal-scroll")
const btnScrollLeft = document.querySelector("#hourly-btn-scroll-left")
const btnScrollRight = document.querySelector("#hourly-btn-scroll-right")
let maxScroll = -sConst.offsetWidth + hScroll.offsetWidth;
btnScrollLeft.style.cursor = 'auto'
btnScrollLeft.style.transition = 'none'
btnScrollLeft.style.opacity = '0';
function scrollHorizontally(val){
  btnScrollLeft.style.transition - '0.5s'
  currentScrollPosition += (val * scrollAmount);
  if (currentScrollPosition > 0){
    currentScrollPosition = 0;
    btnScrollLeft.style.cursor = 'auto'
    btnScrollLeft.style.opacity = '0';
  }else{
    btnScrollLeft.style.cursor = 'pointer'
    btnScrollLeft.style.opacity = '.7';
  }
  if(currentScrollPosition < maxScroll){
    currentScrollPosition = maxScroll;
    btnScrollRight.style.opacity = '0';
    btnScrollRight.style.cursor = 'auto'
  }else{
    btnScrollRight.style.opacity = '.7';
    btnScrollRight.style.cursor = 'pointer'
  }
  sConst.style.left = currentScrollPosition + "px";
}

let dCurrentScrollPosition = 0;
let dScrollAmount = 320;
const dSConst = document.querySelector(".daily-container")
const dHScroll = document.querySelector(".daily-horizontal-scroll")
const dBtnScrollLeft = document.querySelector("#daily-btn-scroll-left")
const dBtnScrollRight = document.querySelector("#daily-btn-scroll-right")
let dMaxScroll = -dSConst.offsetWidth + dHScroll.offsetWidth;
dBtnScrollLeft.style.cursor = 'auto'
dBtnScrollLeft.style.transition = 'none'
dBtnScrollLeft.style.opacity = '0';
function dScrollHorizontally(val){
  dCurrentScrollPosition += (val * dScrollAmount);
  dBtnScrollLeft.style.transition = '0.5s'
  if (dCurrentScrollPosition > 0){
    dCurrentScrollPosition = 0;
    dBtnScrollLeft.style.cursor = 'auto'
    dBtnScrollLeft.style.opacity = '0';
  }else{
    dBtnScrollLeft.style.cursor = 'pointer'
    dBtnScrollLeft.style.opacity = '.7';
  }
  if(dCurrentScrollPosition < dMaxScroll){
    dCurrentScrollPosition = dMaxScroll;
    dBtnScrollRight.style.opacity = '0';
    dBtnScrollRight.style.cursor = 'auto'
  }else{
    dBtnScrollRight.style.opacity = '.7';
    dBtnScrollRight.style.cursor = 'pointer'
  }
  dSConst.style.left = dCurrentScrollPosition + "px";
}
