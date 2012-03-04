function putImage(image){
  var h = document.getElementById('imageHolder');
  while(h.firstChild){
    h.removeChild(h.firstChild);
  }
  h.appendChild(image);
}

function loadImage1(){
var loadingPanel = new yuiLoadingPanel();

var loader = new ImageLoader('http://test.thecodecentral.com/demos/imageloader/Tree.jpg');
loadingPanel.show('Loading Image...');
loader.loadEvent = function(url, image){
  putImage(image);
  loadingPanel.hide();
}
loader.load();
}


function setStatusText(text, id){
  var t = document.getElementById(id);
  while(t.firstChild){
    t.removeChild(t.firstChild);
  }

  t.appendChild(document.createTextNode(text));
}

function loadImage2(){
var loader = new ImageLoader('http://test.thecodecentral.com/demos/imageloader/Garden.jpg');
setStatusText('loading image...', 'status');
loader.loadEvent = function(url, image){
  setStatusText(url + ' loaded', 'status');
  putImage(image);
}
loader.load();
}


function loadImage3(){
var txtUrl = document.getElementById('url');
var loader = new ImageLoader(txtUrl.value);
setStatusText('loading image...', 'status2');
loader.loadEvent = function(url, image){
  setStatusText(url + ' loaded', 'status2');
  putImage(image);
}
loader.load();
}
