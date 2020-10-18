let scene, camera, renderer, hlight, controls;

function init() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xdddddd);

    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);

    camera = new THREE.PerspectiveCamera(
        40,
        window.innerWidth / window.innerHeight,
        1,
        5000
    );
    camera.position.z = 1000;
    camera.position.x = 200;
    camera.position.y = 100;

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.update();

    // Lights
    hlight = new THREE.AmbientLight(0x404040, 50);
    scene.add(hlight);

    directionalLight = new THREE.DirectionalLight(0xffffff, 50);
    directionalLight.position.set(0, 1, 0);
    directionalLight.castShadow = true;
    scene.add(directionalLight);
    light = new THREE.PointLight(0xc4c4c4, 10);
    light.position.set(0, 1, 1);
    scene.add(light);
    light2 = new THREE.PointLight(0xc4c4c4, 10);
    light2.position.set(1, 1, 0);
    scene.add(light2);
    light3 = new THREE.PointLight(0xc4c4c4, 10);
    light3.position.set(0, 11, -11);
    scene.add(light3);
    light4 = new THREE.PointLight(0xc4c4c4, 10);
    light4.position.set(-500, 300, 500);
    scene.add(light4);

    document.body.appendChild(renderer.domElement);
    window.addEventListener("resize", () => {
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
    });

    let loader = new THREE.GLTFLoader();
    loader.load(
        "../models/scene.gltf",
        function(gltf) {
            car = gltf.scene.children[0];
            car.scale.set(1, 1, 1);
            scene.add(gltf.scene);
            renderer.render(scene, camera);
            animate();
        },
        function(xhr) {
            console.log((xhr.loaded / xhr.total * 100) + '% loaded');
        },
        function(err) {
            console.error('An error happened', err);
        },
        null
    );
}

function animate() {

    requestAnimationFrame(animate);

    // required if controls.enableDamping or controls.autoRotate are set to true
    controls.update();

    renderer.render(scene, camera);

}

init();