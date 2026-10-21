(globalThis.TURBOPACK || (globalThis.TURBOPACK = [])).push([
  "object" == typeof document ? document.currentScript : void 0,
  166950,
  (e) => {
    "use strict";
    var t = e.i(101685);
    function r(e, t) {
      let r;
      return (...n) => {
        window.clearTimeout(r), (r = window.setTimeout(() => e(...n), t));
      };
    }
    let n = ["x", "y", "top", "bottom", "left", "right", "width", "height"];
    e.s([
      "default",
      0,
      function (
        { debounce: e, scroll: a, polyfill: i, offsetSize: o } = {
          debounce: 0,
          scroll: !1,
          offsetSize: !1,
        }
      ) {
        var s, l, u;
        let c = i || ("u" < typeof window ? class {} : window.ResizeObserver);
        if (!c)
          throw Error(
            "This browser does not support ResizeObserver out of the box. See: https://github.com/react-spring/react-use-measure/#resize-observer-polyfills"
          );
        let [d, f] = (0, t.useState)({
            left: 0,
            top: 0,
            width: 0,
            height: 0,
            bottom: 0,
            right: 0,
            x: 0,
            y: 0,
          }),
          m = (0, t.useRef)({
            element: null,
            scrollContainers: null,
            resizeObserver: null,
            lastBounds: d,
            orientationHandler: null,
          }),
          v = e ? ("number" == typeof e ? e : e.scroll) : null,
          p = e ? ("number" == typeof e ? e : e.resize) : null,
          h = (0, t.useRef)(!1);
        (0, t.useEffect)(() => ((h.current = !0), () => void (h.current = !1)));
        let [L, w, g] = (0, t.useMemo)(() => {
          let e = () => {
            let e, t;
            if (!m.current.element) return;
            let {
                left: r,
                top: a,
                width: i,
                height: s,
                bottom: l,
                right: u,
                x: c,
                y: d,
              } = m.current.element.getBoundingClientRect(),
              v = {
                left: r,
                top: a,
                width: i,
                height: s,
                bottom: l,
                right: u,
                x: c,
                y: d,
              };
            m.current.element instanceof HTMLElement &&
              o &&
              ((v.height = m.current.element.offsetHeight),
              (v.width = m.current.element.offsetWidth)),
              Object.freeze(v),
              h.current &&
                ((e = m.current.lastBounds),
                (t = v),
                !n.every((r) => e[r] === t[r])) &&
                f((m.current.lastBounds = v));
          };
          return [e, p ? r(e, p) : e, v ? r(e, v) : e];
        }, [f, o, v, p]);
        function b() {
          m.current.scrollContainers &&
            (m.current.scrollContainers.forEach((e) =>
              e.removeEventListener("scroll", g, !0)
            ),
            (m.current.scrollContainers = null)),
            m.current.resizeObserver &&
              (m.current.resizeObserver.disconnect(),
              (m.current.resizeObserver = null)),
            m.current.orientationHandler &&
              ("orientation" in screen &&
              "removeEventListener" in screen.orientation
                ? screen.orientation.removeEventListener(
                    "change",
                    m.current.orientationHandler
                  )
                : "onorientationchange" in window &&
                  window.removeEventListener(
                    "orientationchange",
                    m.current.orientationHandler
                  ));
        }
        function y() {
          m.current.element &&
            ((m.current.resizeObserver = new c(g)),
            m.current.resizeObserver.observe(m.current.element),
            a &&
              m.current.scrollContainers &&
              m.current.scrollContainers.forEach((e) =>
                e.addEventListener("scroll", g, { capture: !0, passive: !0 })
              ),
            (m.current.orientationHandler = () => {
              g();
            }),
            "orientation" in screen && "addEventListener" in screen.orientation
              ? screen.orientation.addEventListener(
                  "change",
                  m.current.orientationHandler
                )
              : "onorientationchange" in window &&
                window.addEventListener(
                  "orientationchange",
                  m.current.orientationHandler
                ));
        }
        return (
          (s = g),
          (l = !!a),
          (0, t.useEffect)(() => {
            if (l)
              return (
                window.addEventListener("scroll", s, {
                  capture: !0,
                  passive: !0,
                }),
                () => void window.removeEventListener("scroll", s, !0)
              );
          }, [s, l]),
          (u = w),
          (0, t.useEffect)(
            () => (
              window.addEventListener("resize", u),
              () => void window.removeEventListener("resize", u)
            ),
            [u]
          ),
          (0, t.useEffect)(() => {
            b(), y();
          }, [a, g, w]),
          (0, t.useEffect)(() => b, []),
          [
            (e) => {
              e &&
                e !== m.current.element &&
                (b(),
                (m.current.element = e),
                (m.current.scrollContainers = (function e(t) {
                  let r = [];
                  if (!t || t === document.body) return r;
                  let {
                    overflow: n,
                    overflowX: a,
                    overflowY: i,
                  } = window.getComputedStyle(t);
                  return (
                    [n, a, i].some((e) => "auto" === e || "scroll" === e) &&
                      r.push(t),
                    [...r, ...e(t.parentElement)]
                  );
                })(e)),
                y());
            },
            d,
            L,
          ]
        );
      },
    ]);
  },
  57152,
  (e) => {
    "use strict";
    var t = e.i(101685);
    let r = new WeakMap();
    e.s([
      "useOverlayBackgroundInert",
      0,
      function (e, n = "smooth-wrapper") {
        (0, t.useEffect)(() => {
          if (!e) return;
          let t = document.getElementById(n);
          if (!t) return;
          let a = r.get(t);
          return (
            a
              ? (a.count += 1)
              : (r.set(t, {
                  count: 1,
                  hadInert: t.hasAttribute("inert"),
                  previousAriaHidden: t.getAttribute("aria-hidden"),
                }),
                t.setAttribute("inert", ""),
                t.setAttribute("aria-hidden", "true")),
            () => {
              let e = r.get(t);
              !e ||
                ((e.count -= 1),
                e.count > 0 ||
                  (e.hadInert || t.removeAttribute("inert"),
                  null === e.previousAriaHidden
                    ? t.removeAttribute("aria-hidden")
                    : t.setAttribute("aria-hidden", e.previousAriaHidden),
                  r.delete(t)));
            }
          );
        }, [e, n]);
      },
    ]);
  },
  964922,
  (e) => {
    "use strict";
    var t = e.i(44501),
      r = e.i(81090),
      n = e.i(732919),
      a = e.i(543340),
      i = e.i(234022),
      o = e.i(101685),
      s = e.i(83629),
      l = e.i(91285);
    let u = null,
      c = {
        1: {
          path: "M 14 0 L 30 0 L 41 11 L 197 11 L 208 0 L 368 0 L 384 16 L 384 125 L 359 150 L 201.34 150 L 194.34 143 L 46.34 143 L 39.34 150 L 0 150 L 0 14 Z",
          viewBox: "0 0 384 150",
          accents: [
            { d: "M 16 -5 L 5 -16 L 16 -16 Z", transform: "translate(368 16)" },
            { d: "M 25 5 L 5 25 L 25 25 Z", transform: "translate(359 125)" },
          ],
        },
        2: {
          path: "M 21 0 L 181 0 L 186 5 L 348 5 L 353 0 L 369 0 L 384 15 L 384 129 L 363 150 L 245.86 150 L 236.86 159 L 130.86 159 L 121.86 150 L 26 150 L 0 124 L 0 21 Z",
          viewBox: "0 0 384 159",
          accents: [
            {
              d: "M -21 -5 L -5 -21 L -21 -21 Z",
              transform: "translate(21 21)",
            },
            { d: "M 21 5 L 5 21 L 21 21 Z", transform: "translate(363 129)" },
          ],
        },
        3: {
          path: "M 37 0 L 53 0 L 61 -8 L 168 -8 L 176 0 L 366 0 L 384 18 L 384 150 L 0 150 L 0 37 Z",
          viewBox: "0 -10 384 165",
          accents: [
            { d: "M 18 -5 L 5 -18 L 18 -18 Z", transform: "translate(366 18)" },
            { d: "M 0 0 L 0 -20 L -20 0 Z", transform: "translate(380 146)" },
            { d: "M 0 0 L 16 0 L 0 -16 Z", transform: "translate(4 146)" },
          ],
        },
        4: {
          path: "M 18 0 L 146 0 L 155 9 L 343 9 L 352 0 L 368 0 L 384 16 L 384 68 L 378 74 L 378 105 L 384 111 L 384 127 L 361 150 L 14 150 L 0 136 L 0 18 Z",
          viewBox: "0 0 384 150",
          accents: [
            { d: "M 16 -5 L 5 -16 L 16 -16 Z", transform: "translate(368 16)" },
            { d: "M 23 5 L 5 23 L 23 23 Z", transform: "translate(361 127)" },
          ],
        },
        5: {
          path: "M 23 0 L 368 0 L 384 16 L 384 32 L 398 46 L 398 87 L 384 101 L 384 150 L 368 150 L 353 135 L 248 135 L 233 150 L 30 150 L 0 120 L 0 23 Z",
          viewBox: "0 0 398 150",
          accents: [
            {
              d: "M -23 -5 L -5 -23 L -23 -23 Z",
              transform: "translate(23 23)",
            },
            { d: "M 0 0 L 0 -12 L -12 0 Z", transform: "translate(380 146)" },
          ],
        },
        6: {
          path: "M 15 0 L 369 0 L 384 15 L 384 50 L 374 60 L 374 90 L 384 100 L 384 135 L 369 150 L 15 150 L 0 135 L 0 100 L 10 90 L 10 60 L 0 50 L 0 15 Z",
          viewBox: "0 0 384 150",
          overflowVisible: !0,
          accents: [
            { d: "M 0 0 L 11 0 L 11 11 Z", transform: "translate(373 0)" },
            { d: "M 0 11 L 11 0 L 11 11 Z", transform: "translate(373 139)" },
            { d: "M 0 0 L 11 0 L 0 11 Z", transform: "translate(0 0)" },
            { d: "M 0 0 L 11 11 L 0 11 Z", transform: "translate(0 139)" },
          ],
        },
        7: {
          path: "M 18 0 L 384 0 L 384 132 L 366 150 L 130 150 L 121 141 L 28 141 L 19 150 L 0 150 L 0 18 Z",
          viewBox: "0 0 384 150",
          accents: [
            { d: "M 18 5 L 5 18 L 18 18 Z", transform: "translate(366 132)" },
            {
              d: "M -18 -5 L -5 -18 L -18 -18 Z",
              transform: "translate(18 18)",
            },
          ],
        },
        8: {
          path: "M 21 0 L 181 0 L 186 5 L 348 5 L 353 0 L 369 0 L 384 15 L 384 129 L 363 150 L 267 150 L 249 122 L 135 122 L 117 150 L 26 150 L 0 124 L 0 21 Z",
          viewBox: "0 0 384 150",
          accents: [
            {
              d: "M -21 -5 L -5 -21 L -21 -21 Z",
              transform: "translate(21 21)",
            },
            { d: "M 21 5 L 5 21 L 21 21 Z", transform: "translate(363 129)" },
          ],
        },
      };
    e.s([
      "CyberCard",
      0,
      ({
        children: e,
        className: d,
        containerClassName: f,
        shape: m = 1,
        glowColor: v = "var(--color-primary-500, #14F4E4)",
        glowOpacity: p = 0.4,
        showScanline: h = !0,
        showMatrix: L = !1,
        showNoise: w = !0,
        activeOpacity: g = 0.4,
        hoverScale: b = 1.01,
        animateOnMount: y = !0,
        backgroundColor: x,
        isStatic: R = !1,
        disableFrameAnimation: C = !1,
        lean: M = !1,
        glass: k = !1,
      }) => {
        let E,
          [N, I] = (0, o.useState)(() => u ?? !1);
        (0, o.useEffect)(() => {
          null === u && (u = (0, s.shouldUseLowEndRenderMode)()),
            u !== N && I(u);
        }, [N]);
        let j = M || N,
          Z = R || j,
          T = C || j,
          A = !j && h,
          B = !j && w,
          z = !j && L,
          F = x || (j ? "rgba(5, 5, 5, 0.96)" : "rgba(0, 10, 15, 0.4)"),
          H = (E = F.match(
            /^rgba?\(\s*[\d.]+\s*,\s*[\d.]+\s*,\s*[\d.]+\s*(?:,\s*([\d.]+)\s*)?\)$/i
          ))
            ? void 0 === E[1]
              ? 1
              : Number.parseFloat(E[1])
            : null,
          D = !j && !k && (null === H || H < 0.9),
          S = Z || T || !y || j,
          [O, P] = (0, o.useState)(S),
          $ = c[m],
          U = (0, o.useRef)(null),
          W = (0, o.useRef)(null),
          V = (0, o.useRef)(null),
          Y = Z || T;
        (0, o.useEffect)(() => {
          P(!0);
        }, []),
          (0, o.useEffect)(() => {
            if (!O || j) return;
            n.gsap.registerPlugin(a.ScrollTrigger);
            let e = n.gsap.context(() => {
              if (!W.current || !V.current) return;
              let e = W.current.getTotalLength(),
                t = U.current?.querySelectorAll(".cyber-accent");
              if (T) {
                n.gsap.set([W.current, V.current], {
                  strokeDasharray: e,
                  strokeDashoffset: 0,
                }),
                  n.gsap.set(V.current, { opacity: 0 }),
                  t && n.gsap.set(t, { scale: 1, opacity: 0.8, rotation: 0 });
                return;
              }
              if (Z) {
                n.gsap.set([W.current, V.current], {
                  strokeDasharray: e,
                  strokeDashoffset: 0,
                }),
                  t && n.gsap.set(t, { scale: 1, opacity: 0.8, rotation: 0 });
                return;
              }
              n.gsap.set([W.current, V.current], {
                strokeDasharray: e,
                strokeDashoffset: e,
              }),
                t && n.gsap.set(t, { scale: 0, opacity: 0, rotation: -45 });
              let r = n.gsap.timeline({
                scrollTrigger: {
                  trigger: U.current,
                  start: "top 85%",
                  toggleActions: "play none none none",
                },
              });
              r.to(W.current, {
                strokeDashoffset: 0,
                duration: 2,
                ease: "power2.inOut",
              }),
                t &&
                  t.length > 0 &&
                  r.to(
                    t,
                    {
                      scale: 1,
                      opacity: 0.8,
                      rotation: 0,
                      duration: 0.8,
                      ease: "back.out(1.7)",
                    },
                    "-=0.5"
                  ),
                r.to(
                  V.current,
                  { strokeDashoffset: 0, duration: 1.5, ease: "power1.inOut" },
                  "-=1"
                );
            }, U);
            return () => e.revert();
          }, [j, T, O, Z]);
        let q = O
            ? {
                clipPath: ((e, t) => {
                  let r = t.trim().split(/\s+/),
                    n = parseFloat(r[0]) || 0,
                    a = parseFloat(r[1]) || 0,
                    i = parseFloat(r[2]) || 384,
                    o = parseFloat(r[3]) || 150,
                    s = e.replace(/[MLZ]/g, " ").trim().split(/\s+/),
                    l = [];
                  for (let e = 0; e < s.length; e += 2) {
                    let t = parseFloat(s[e]),
                      r = parseFloat(s[e + 1]);
                    if (Number.isNaN(t) || Number.isNaN(r)) continue;
                    let u = ((t - n) / i) * 100,
                      c = ((r - a) / o) * 100;
                    l.push(`${u.toFixed(3)}% ${c.toFixed(3)}%`);
                  }
                  return `polygon(${l.join(", ")})`;
                })($.path, $.viewBox),
              }
            : void 0,
          [_, G, K, X] = $.viewBox.split(" ").map(Number),
          J = `${_ - 3.5} ${G - 3.5} ${K + 7} ${X + 7}`,
          Q = (0, l.cn)("relative group transition-all duration-700", f),
          ee = (0, t.jsxs)(t.Fragment, {
            children: [
              (0, t.jsxs)("div", {
                className:
                  "absolute inset-0 z-0 pointer-events-none overflow-hidden",
                style: q,
                children: [
                  D &&
                    (0, t.jsx)("div", {
                      className:
                        "absolute inset-0 backdrop-blur-md bg-transparent",
                      style: q,
                    }),
                  k &&
                    (0, t.jsx)("div", {
                      className:
                        "absolute inset-0 bg-black/15 backdrop-blur-[12px] backdrop-saturate-125",
                      style: q,
                    }),
                  (0, t.jsx)("div", {
                    className: (0, l.cn)(
                      "absolute inset-0 transition-opacity duration-1000",
                      Z ? "opacity-100" : "group-hover:opacity-100"
                    ),
                    style: { opacity: Z || j ? 1 : g },
                    children:
                      O &&
                      (0, t.jsx)("svg", {
                        className: "w-full h-full",
                        viewBox: $.viewBox,
                        preserveAspectRatio: "none",
                        fill: "none",
                        xmlns: "http://www.w3.org/2000/svg",
                        "aria-hidden": "true",
                        children: (0, t.jsx)("path", {
                          d: $.path,
                          fill: F,
                          vectorEffect: "non-scaling-stroke",
                          className: Y
                            ? void 0
                            : "transition-colors duration-700",
                        }),
                      }),
                  }),
                  B &&
                    (0, t.jsx)("div", {
                      className: "absolute inset-0 cyber-noise opacity-[0.03]",
                    }),
                  A &&
                    (0, t.jsx)("div", {
                      className: "absolute inset-0 overflow-hidden",
                      children: (0, t.jsx)("div", {
                        className:
                          "w-full h-[1px] bg-primary-500/10 absolute top-0 animate-scanline",
                      }),
                    }),
                  z &&
                    O &&
                    (0, t.jsx)("div", {
                      className: "absolute inset-0 overflow-hidden opacity-10",
                      children: ["m1", "m2", "m3", "m4", "m5", "m6"].map(
                        (e, r) =>
                          (0, t.jsx)(
                            "div",
                            {
                              className:
                                "absolute w-px bg-primary-400 animate-matrix-drop",
                              style: {
                                left: `${15 + 15 * r}%`,
                                height: `${20 + 40 * Math.random()}%`,
                                animationDelay: `${2 * Math.random()}s`,
                                animationDuration: `${
                                  1.5 + 2 * Math.random()
                                }s`,
                              },
                            },
                            e
                          )
                      ),
                    }),
                ],
              }),
              (0, t.jsx)("div", {
                className: (0, l.cn)("relative z-10", d),
                children: e,
              }),
              (0, t.jsx)("div", {
                className: (0, l.cn)(
                  "absolute inset-0 z-20 pointer-events-none transition-opacity duration-1000 overflow-visible",
                  Z ? "opacity-100" : "group-hover:opacity-100"
                ),
                style: { opacity: Z || j ? 1 : p },
                children:
                  O &&
                  (0, t.jsxs)("svg", {
                    className: "w-full h-full overflow-visible",
                    viewBox: J,
                    preserveAspectRatio: "none",
                    fill: "none",
                    xmlns: "http://www.w3.org/2000/svg",
                    "aria-hidden": "true",
                    children: [
                      (0, t.jsx)("path", {
                        ref: W,
                        d: $.path,
                        fill: "none",
                        stroke: v,
                        strokeWidth: "1.2",
                        className: Y
                          ? void 0
                          : "transition-colors duration-700",
                        opacity: j ? 0.42 : 0.3,
                      }),
                      (0, t.jsx)("path", {
                        ref: V,
                        d: $.path,
                        fill: "none",
                        stroke: v,
                        strokeWidth: "2.2",
                        strokeLinecap: "round",
                        className: Y
                          ? void 0
                          : "transition-colors duration-700",
                        opacity: T || j ? 0 : 0.8,
                      }),
                      $.accents.map((e) =>
                        (0, t.jsx)(
                          "path",
                          {
                            d: e.d,
                            transform: e.transform,
                            fill: v,
                            className: "origin-center cyber-accent",
                            opacity: j ? 0.55 : void 0,
                          },
                          `${e.transform}-${e.d}`
                        )
                      ),
                    ],
                  }),
              }),
              !j &&
                (0, t.jsx)(r.default, {
                  id: "28bbfcafa9483749",
                  children:
                    "@keyframes scanline{0%{transform:translateY(0)}to{transform:translateY(100vh)}}@keyframes matrix-drop{0%{transform:translateY(-100%)}to{transform:translateY(400%)}}.animate-scanline.jsx-28bbfcafa9483749{animation:8s linear infinite scanline}.animate-matrix-drop.jsx-28bbfcafa9483749{animation:matrix-drop var(--duration,2s) linear infinite}",
                }),
            ],
          });
        return M
          ? (0, t.jsx)("div", { ref: U, className: Q, children: ee })
          : (0, t.jsx)(i.motion.div, {
              ref: U,
              initial: y ? { opacity: 0 } : { opacity: 1 },
              animate: { opacity: 1 },
              whileHover: Z ? void 0 : { scale: b, opacity: 1 },
              className: Q,
              children: ee,
            });
      },
    ]);
  },
  646514,
  (e) => {
    "use strict";
    let t = (0, e.i(663915).default)("chevron-right", [
      ["path", { d: "m9 18 6-6-6-6", key: "mthhwq" }],
    ]);
    e.s(["ChevronRight", 0, t], 646514);
  },
  629462,
  (e) => {
    "use strict";
    var t = e.i(44501),
      r = e.i(101685),
      n = e.i(946154),
      a = e.i(721348),
      i = e.i(131398);
    let o = 22.22222222222222;
    e.s([
      "RageEffectShader",
      0,
      function ({ hoveredSkill: e, intensity: s, skills: l, containerRef: u }) {
        let c = (0, r.useRef)(null),
          d = (0, r.useRef)(null),
          f = (0, r.useRef)(0),
          m = (0, r.useRef)(null),
          v = (0, r.useRef)(null),
          p = (0, r.useRef)(null),
          h = (0, r.useRef)(null),
          L = (0, i.usePrefersReducedMotion)(),
          w = (0, r.useRef)(e),
          g = (0, r.useRef)(s);
        (0, r.useEffect)(() => {
          (w.current = e), (g.current = s);
        }, [e, s]);
        let b = (0, r.useRef)(!1);
        return (
          (0, r.useEffect)(() => {
            if (!c.current) return;
            let e = c.current,
              t = new n.WebGLRenderer({
                canvas: e,
                alpha: !0,
                antialias: !1,
                powerPreference: "high-performance",
                precision: "mediump",
              }),
              r = new a.Scene(),
              i = new a.OrthographicCamera(-1, 1, 1, -1, 0, 1),
              s = () => {
                if (!u.current) return;
                let r = u.current.getBoundingClientRect(),
                  n = r.width,
                  a = r.height;
                (e.width = +n), (e.height = +a), t.setSize(n, a, !1);
              };
            s(), window.addEventListener("resize", s);
            let y = l.map((e) => new a.Color(e.color)),
              x = l.map(
                (e) => new a.Vector2(e.position.x / 100, 1 - e.position.y / 100)
              ),
              R = (() => {
                let e = new Uint8Array(262144);
                for (let t = 0; t < 65536; t++)
                  (e[4 * t] = 255 * Math.random()),
                    (e[4 * t + 1] = 255 * (0.05 > Math.random())),
                    (e[4 * t + 2] = 255 * Math.random()),
                    (e[4 * t + 3] = 255);
                let t = new a.DataTexture(e, 256, 256, a.RGBAFormat);
                return (
                  (t.wrapS = a.RepeatWrapping),
                  (t.wrapT = a.RepeatWrapping),
                  (t.minFilter = a.LinearFilter),
                  (t.magFilter = a.LinearFilter),
                  (t.needsUpdate = !0),
                  t
                );
              })(),
              C = new a.ShaderMaterial({
                uniforms: {
                  uTime: { value: 0 },
                  uResolution: { value: new a.Vector2(e.width, e.height) },
                  uChakraColors: { value: y },
                  uChakraPositions: { value: x },
                  uHoveredIndex: { value: null !== w.current ? w.current : -1 },
                  uIntensity: { value: g.current },
                  uRageIntensity: { value: 0.4 },
                  uNoiseTexture: { value: R },
                },
                vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
                fragmentShader: `
        uniform float uTime;
        uniform vec2 uResolution;
        uniform vec3 uChakraColors[7];
        uniform vec2 uChakraPositions[7];
        uniform int uHoveredIndex;
        uniform float uIntensity;
        uniform float uRageIntensity;
        uniform sampler2D uNoiseTexture;
        
        varying vec2 vUv;
        
        float getNoise(vec2 p) {
          return texture2D(uNoiseTexture, p).r;
        }

        float getVoronoi(vec2 p) {
          return texture2D(uNoiseTexture, p).g;
        }

        vec3 createRageEffect(vec2 uv, vec2 position, vec3 color, float time, float intensity) {
          float dist = distance(uv, position);
          float baseRadius = 0.08 + 0.04 * sin(time * 1.0);
          
          float mainCircle = 1.0 - smoothstep(baseRadius - 0.02, baseRadius + 0.01, dist);
          mainCircle = pow(mainCircle, 6.0);
          
          float core = 1.0 - smoothstep(baseRadius * 0.3 - 0.01, baseRadius * 0.3 + 0.01, dist);
          
          float noiseLookup = getNoise(uv * 2.5 + time * 0.1);
          float vNoise = getVoronoi(uv * 3.0 - time * 0.05);
          
          float pulse = 0.7 + 0.3 * sin(time * 1.0 + dist * 8.0);
          float flicker = 0.9 + 0.1 * sin(time * 25.0 + noiseLookup * 10.0);
          
          return color * (mainCircle + core * 1.2 + vNoise * mainCircle * 0.4) * pulse * flicker * intensity * uRageIntensity;
        }

        void main() {
          vec3 finalColor = vec3(0.0);
          
          if(uHoveredIndex >= 0 && uHoveredIndex < 7) {
            int index = uHoveredIndex;
            vec2 chakraPos = uChakraPositions[index];
            vec3 chakraColor = uChakraColors[index];
            
            finalColor += createRageEffect(vUv, chakraPos, chakraColor, uTime, 1.2);
            
            for(int wave = 0; wave < 3; wave++) {
              float waveRadius = 0.1 + float(wave) * 0.1 + sin(uTime * 0.8 + float(wave)) * 0.02;
              float waveDist = distance(vUv, chakraPos);
              float waveEffect = smoothstep(waveRadius + 0.08, waveRadius - 0.08, waveDist) * (1.0 - smoothstep(waveRadius - 0.03, waveRadius + 0.03, waveDist));
              finalColor += chakraColor * pow(waveEffect, 0.5) * 0.12 * exp(-float(wave) * 0.5);
            }
            
            float auraDist = distance(vUv, chakraPos);
            float aura = (1.0 - smoothstep(0.0, 0.7, auraDist)) * 0.15;
            finalColor += chakraColor * aura * getNoise(vUv * 1.5 + uTime * 0.05);

          } else {
            for(int i = 0; i < 7; i++) {
                float d = distance(vUv, uChakraPositions[i]);
                float g = 1.0 - smoothstep(0.0, 0.15, d);
                finalColor += uChakraColors[i] * g * 0.12 * uRageIntensity;
            }
          }
          
          float alpha = min(length(finalColor) * 0.8, 0.7);
          gl_FragColor = vec4(finalColor, alpha);
        }
      `,
                transparent: !0,
                blending: a.AdditiveBlending,
                depthTest: !1,
                depthWrite: !1,
              }),
              M = new a.PlaneGeometry(2, 2),
              k = new a.Mesh(M, C);
            r.add(k);
            let E = new a.Timer();
            if (L)
              return (
                (C.uniforms.uTime.value = 0),
                C.uniforms.uResolution.value.set(e.width, e.height),
                (C.uniforms.uHoveredIndex.value =
                  null !== w.current ? w.current : -1),
                (C.uniforms.uIntensity.value = g.current),
                t.render(r, i),
                (m.current = t),
                (v.current = r),
                (p.current = i),
                (h.current = C),
                () => {
                  window.removeEventListener("resize", s), E.dispose();
                  try {
                    C.dispose(), R.dispose(), t.dispose(), M.dispose();
                  } catch (e) {}
                }
              );
            let N = (n) => {
                if (!b.current) {
                  d.current = null;
                  return;
                }
                d.current = requestAnimationFrame(N);
                let a = n - f.current;
                if (a < o) return;
                (f.current = n - (a % o)), E.update(n);
                let s = E.getElapsed();
                (C.uniforms.uTime.value = s),
                  C.uniforms.uResolution.value.set(e.width, e.height),
                  (C.uniforms.uHoveredIndex.value =
                    null !== w.current ? w.current : -1);
                let l = C.uniforms.uIntensity.value,
                  u = g.current;
                (C.uniforms.uIntensity.value = l + (u - l) * 0.1),
                  null !== w.current
                    ? (C.uniforms.uRageIntensity.value = Math.min(
                        C.uniforms.uRageIntensity.value + 0.03,
                        1.2
                      ))
                    : (C.uniforms.uRageIntensity.value = Math.max(
                        C.uniforms.uRageIntensity.value - 0.03,
                        0.6
                      )),
                  t.render(r, i);
              },
              I = new IntersectionObserver(
                (e) => {
                  let t = b.current;
                  (b.current = e[0].isIntersecting),
                    e[0].isIntersecting && !t
                      ? (null !== d.current && cancelAnimationFrame(d.current),
                        (d.current = requestAnimationFrame(N)))
                      : e[0].isIntersecting ||
                        null === d.current ||
                        (cancelAnimationFrame(d.current), (d.current = null));
                },
                { threshold: 0.01 }
              );
            return (
              u.current && I.observe(u.current),
              (m.current = t),
              (v.current = r),
              (p.current = i),
              (h.current = C),
              b.current && N(performance.now()),
              () => {
                I.disconnect(),
                  d.current &&
                    (cancelAnimationFrame(d.current), (d.current = null)),
                  window.removeEventListener("resize", s),
                  E.dispose();
                try {
                  C.dispose(), R.dispose(), t.dispose(), M.dispose();
                } catch (e) {}
              }
            );
          }, [l, u, L]),
          (0, t.jsx)("canvas", {
            ref: c,
            className: "absolute inset-0 w-full h-full",
            style: {
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: "100%",
              pointerEvents: "none",
              zIndex: 15,
            },
          })
        );
      },
    ]);
  },
  997706,
  (e) => {
    e.n(e.i(339153));
  },
]);
