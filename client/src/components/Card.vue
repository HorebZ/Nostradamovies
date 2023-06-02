<template>
  <div class="container">
    <div v-for="(image, index) in images" :key="index" class="cover atvImg">
      <div class="atvImg-layer" :data-img="image.backgroundImg"></div>
      <div class="atvImg-layer" :data-img="image.logoImg"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: [
        {
          backgroundImg: "http://robindelaporte.fr/codepen/visa-bg.jpg",
          logoImg: "http://robindelaporte.fr/codepen/visa.png",
        },
        {
          backgroundImg: "http://robindelaporte.fr/codepen/visa-bg-2.jpg",
          logoImg: "http://robindelaporte.fr/codepen/visa.png",
        },
        {
          backgroundImg: "http://robindelaporte.fr/codepen/visa-bg-3.jpg",
          logoImg: "http://robindelaporte.fr/codepen/visa.png",
        },
        {
          backgroundImg: "http://robindelaporte.fr/codepen/visa-bg-4.jpg",
          logoImg: "http://robindelaporte.fr/codepen/visa.png",
        },
      ],
    };
  },
  mounted() {
    this.initializeAtvImg();
  },
  methods: {
    initializeAtvImg() {
      const imgs = document.querySelectorAll(".atvImg");
      const totalImgs = imgs.length;
      if (totalImgs <= 0) {
        return;
      }

      for (let l = 0; l < totalImgs; l++) {
        const thisImg = imgs[l];
        const layerElems = thisImg.querySelectorAll(".atvImg-layer");
        const totalLayerElems = layerElems.length;

        if (totalLayerElems <= 0) {
          continue;
        }

        while (thisImg.firstChild) {
          thisImg.removeChild(thisImg.firstChild);
        }

        const containerHTML = document.createElement("div");
        const shineHTML = document.createElement("div");
        const shadowHTML = document.createElement("div");
        const layersHTML = document.createElement("div");
        const layers = [];

        thisImg.id = "atvImg__" + l;
        containerHTML.className = "atvImg-container";
        shineHTML.className = "atvImg-shine";
        shadowHTML.className = "atvImg-shadow";
        layersHTML.className = "atvImg-layers";

        for (let i = 0; i < totalLayerElems; i++) {
          const layer = document.createElement("div");
          const imgSrc = layerElems[i].getAttribute("data-img");

          layer.className = "atvImg-rendered-layer";
          layer.setAttribute("data-layer", i);
          layer.style.backgroundImage = `url(${imgSrc})`;
          layersHTML.appendChild(layer);

          layers.push(layer);
        }

        containerHTML.appendChild(shadowHTML);
        containerHTML.appendChild(layersHTML);
        containerHTML.appendChild(shineHTML);
        thisImg.appendChild(containerHTML);

        const w =
          thisImg.clientWidth ||
          thisImg.offsetWidth ||
          thisImg.scrollWidth;
        thisImg.style.transform = `perspective(${w * 3}px)`;

        this.addEventListeners(
          thisImg,
          layers,
          totalLayerElems,
          shineHTML
        );
      }
    },
    addEventListeners(thisImg, layers, totalLayers, shineHTML) {
      const supportsTouch =
        "ontouchstart" in window ||
        navigator.msMaxTouchPoints;

      if (supportsTouch) {
        let preventScroll = false;

        thisImg.addEventListener("touchmove", (e) => {
          if (preventScroll) {
            e.preventDefault();
          }
          this.processMovement(e, true, thisImg, layers, totalLayers, shineHTML);
        });

        thisImg.addEventListener("touchstart", (e) => {
          preventScroll = true;
          this.processEnter(e, thisImg);
        });

        thisImg.addEventListener("touchend", (e) => {
          preventScroll = false;
          this.processExit(e, thisImg, layers, totalLayers, shineHTML);
        });
      } else {
        thisImg.addEventListener("mousemove", (e) => {
          this.processMovement(e, false, thisImg, layers, totalLayers, shineHTML);
        });

        thisImg.addEventListener("mouseenter", (e) => {
          this.processEnter(e, thisImg);
        });

        thisImg.addEventListener("mouseleave", (e) => {
          this.processExit(e, thisImg, layers, totalLayers, shineHTML);
        });
      }
    },
    processMovement(e, touchEnabled, elem, layers, totalLayers, shineHTML) {
      const scrollTop =
        document.body.scrollTop || document.documentElement.scrollTop;
      const scrollLeft = document.body.scrollLeft;
      const pageX = touchEnabled ? e.touches[0].pageX : e.pageX;
      const pageY = touchEnabled ? e.touches[0].pageY : e.pageY;
      const offsets = elem.getBoundingClientRect();
      const w =
        elem.clientWidth || elem.offsetWidth || elem.scrollWidth;
      const h =
        elem.clientHeight || elem.offsetHeight || elem.scrollHeight;
      const wMultiple = 320 / w;
      const offsetX = 0.52 - (pageX - offsets.left - scrollLeft) / w;
      const offsetY = 0.52 - (pageY - offsets.top - scrollTop) / h;
      const dy = pageY - offsets.top - scrollTop - h / 2;
      const dx = pageX - offsets.left - scrollLeft - w / 2;
      const yRotate = (offsetX - dx) * (0.07 * wMultiple);
      const xRotate = (dy - offsetY) * (0.1 * wMultiple);
      let imgCSS = `rotateX(${xRotate}deg) rotateY(${yRotate}deg)`;
      const arad = Math.atan2(dy, dx);
      let angle = (arad * 180) / Math.PI - 90;

      if (angle < 0) {
        angle = angle + 360;
      }

      if (elem.firstChild.className.indexOf(" over") !== -1) {
        imgCSS += " scale3d(1.07,1.07,1.07)";
      }
      elem.firstChild.style.transform = imgCSS;

      shineHTML.style.background = `linear-gradient(${angle}deg, rgba(255,255,255,${
        (pageY - offsets.top - scrollTop) / h * 0.4
      }) 0%,rgba(255,255,255,0) 80%)`;
      shineHTML.style.transform = `translateX(${
        offsetX * totalLayers - 0.1
      }px) translateY(${offsetY * totalLayers - 0.1}px)`;

      let revNum = totalLayers;
      for (let ly = 0; ly < totalLayers; ly++) {
        layers[ly].style.transform = `translateX(${
          offsetX * revNum * ((ly * 2.5) / wMultiple)
        }px) translateY(${
          offsetY * totalLayers * ((ly * 2.5) / wMultiple)
        }px)`;
        revNum--;
      }
    },
    processEnter(e, elem) {
      elem.firstChild.className += " over";
    },
    processExit(e, elem, layers, totalLayers, shineHTML) {
      const container = elem.firstChild;

      container.className = container.className.replace(" over", "");
      container.style.transform = "";
      shineHTML.style.cssText = "";

      for (let ly = 0; ly < totalLayers; ly++) {
        layers[ly].style.transform = "";
      }
    },
  },
};
</script>

<style scoped>
body {
  background: #99aeff;
}

.container {
  width: 704px;
  height: 460px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.cover {
  display: inline-block;
  height: 200px;
  width: 320px;
  margin: 15px;
  border-radius: 8px;
}

@media screen and (max-width: 700px) {
  .container {
    width: 100%;
    position: relative;
    transform: translate(0%, 0%);
    top: 0;
    left: 0;
  }
  .cover {
    display: block;
    height: 200px;
    width: 320px;
    margin: 15px auto;
  }
}

.atvImg {
  border-radius: 8px;
  transform-style: preserve-3d;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

.atvImg img {
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(14, 21, 47, 0.25);
}

.atvImg-container {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 8px;
  transition: all 0.2s ease-out;
}

.atvImg-container.over .atvImg-shadow {
  box-shadow: 0 45px 100px rgba(14, 21, 47, 0.4), 0 16px 40px rgba(14, 21, 47, 0.4);
}

.atvImg-layers {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 8px;
  overflow: hidden;
  transform-style: preserve-3d;
}

.atvImg-rendered-layer {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0%;
  left: 0%;
  background-repeat: no-repeat;
  background-position: center;
  background-color: transparent;
  background-size: cover;
  transition: all 0.1s ease-out;
  overflow: hidden;
  border-radius: 8px;
}

.atvImg-shadow {
  position: absolute;
  top: 5%;
  left: 5%;
  width: 90%;
  height: 90%;
  transition: all 0.2s ease-out;
  box-shadow: 0 8px 30px rgba(14, 21, 47, 0.6);
}

.atvImg-shine {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 8px;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.35) 50%, rgba(255, 255, 255, 0) 100%);
  transition: all 0.2s ease-out;
  pointer-events: none;
}
</style>
