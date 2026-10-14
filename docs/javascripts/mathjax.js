/* this file is a bunch of AI-generated shit cause latex only worked occasionally*/

component$.subscribe(({ ref }) => {
  if (ref.classList.contains("md-annotation"))
    MathJax.typesetPromise([ref])
})

window.MathJax = {
  loader: {
    load: ["[tex]/html", "[tex]/color"]
  },
  tex: {
    packages: {
      "[+]": ["html", "color"]
    },
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

let mathJaxQueue = Promise.resolve();

function typesetMath(elements) {
  mathJaxQueue = mathJaxQueue
    .then(() => MathJax.typesetPromise(elements))
    .catch(error => console.error("MathJax typesetting failed:", error));

  return mathJaxQueue;
}

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();

  typesetMath();
});

component$.subscribe(({ ref }) => {
  if (ref.classList.contains("md-annotation")) {
    typesetMath([ref]);
  }
});
