let gyroscope = new Gyroscope({ frequency: 60 });


const gxElement = document.getElementById("gx");
const gyElement = document.getElementById("gy");
const gzElement = document.getElementById("gz");

gyroscope.start();
gyroscope.addEventListener("reading", (e) => {
    gxElement.innerHTML = gyroscope.x;
    gyElement.innerHTML = gyroscope.y;
    gzElement.innerHTML = gyroscope.z;
});
