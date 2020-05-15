var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.z = 5;

var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
window.addEventListener("resize", () => {
  renderer.setSize(window.innerWidth, window.innerHeight);
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
});

// Shapes
var geo = new THREE.SphereGeometry(1, 10, 10);
var material = new THREE.MeshLambertMaterial({ color: "#fffbde" });
var mesh = new THREE.Mesh(geo, material);
scene.add(mesh);

// Light
var light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(2, 2, -2);
scene.add(light);

// Load Model
var THREE = window.THREE = require('three');
require('three/examples/js/loaders/OBJLoader2');
// instantiate the loader
let loader = new OBJLoader2();

// function called on successful load
function callbackOnLoad(object3d) {
  scene.add(object3d);
}

// load a resource from provided URL synchronously
loader.load(
  "../models/Low_Poly_City_Cars.obj",
  callbackOnLoad,
  null,
  null,
  null
);

const render = () => {
  requestAnimationFrame(render);
  mesh.rotation.x += 0.05;
  renderer.render(scene, camera);
};

render();
