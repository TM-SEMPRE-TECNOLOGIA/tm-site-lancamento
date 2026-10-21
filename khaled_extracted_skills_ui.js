(globalThis.TURBOPACK || (globalThis.TURBOPACK = [])).push([
  "object" == typeof document ? document.currentScript : void 0,
  339153,
  (e) => {
    "use strict";
    var t = e.i(44501),
      a = e.i(732919),
      s = e.i(543340),
      r = e.i(646514),
      l = e.i(42776);
    let i = (0, e.i(663915).default)("panels-top-left", [
      [
        "rect",
        { width: "18", height: "18", x: "3", y: "3", rx: "2", key: "afitv7" },
      ],
      ["path", { d: "M3 9h18", key: "1pudct" }],
      ["path", { d: "M9 21V9", key: "1oto5p" }],
    ]);
    var n = e.i(355083),
      o = e.i(252587),
      c = e.i(763250),
      d = e.i(101685),
      u = e.i(629462),
      p = e.i(964922),
      m = e.i(916430),
      h = e.i(501024),
      f = e.i(83629),
      x = e.i(841447),
      y = e.i(57152),
      g = e.i(34334),
      b = e.i(475669),
      v = e.i(91285);
    let k = (e) => Math.min(Math.max(Math.ceil(e / 8.333333333333334), 1), 12),
      w = (e) => {
        let t = k(e);
        return t >= 11
          ? "Daily Driver"
          : t >= 9
          ? "Ship With It"
          : t >= 7
          ? "Comfortable"
          : t >= 5
          ? "Getting There"
          : t >= 3
          ? "Learning"
          : "Curious";
      };
    function j({
      level: e,
      color: a,
      size: s = 40,
      isMaxed: r = !1,
      disableAnimations: l = !1,
    }) {
      let i = Math.min(Math.max(e, 1), 12),
        n = {
          1: {
            pulseOpacity: [0.3, 0.7],
            pulseScale: [1, 1.05],
            centerOpacity: 0.8,
            ringOneOpacity: 0.1,
            ringTwoOpacity: 0,
            ringThreeOpacity: 0,
            tracesOpacity: 0,
            flare: !1,
            duration: 3,
          },
          2: {
            pulseOpacity: [0.4, 0.8],
            pulseScale: [0.95, 1.1],
            centerOpacity: 0.9,
            ringOneOpacity: 0.2,
            ringTwoOpacity: 0,
            ringThreeOpacity: 0,
            tracesOpacity: 0,
            flare: !1,
            duration: 2.5,
          },
          3: {
            pulseOpacity: [0.5, 0.85],
            pulseScale: [0.9, 1.15],
            centerOpacity: 1,
            ringOneOpacity: 0.3,
            ringTwoOpacity: 0,
            ringThreeOpacity: 0,
            tracesOpacity: 0,
            flare: !1,
            duration: 2.2,
          },
          4: {
            pulseOpacity: [0.5, 0.9],
            pulseScale: [0.85, 1.2],
            centerOpacity: 1,
            ringOneOpacity: 0.4,
            ringTwoOpacity: 0.2,
            ringThreeOpacity: 0,
            tracesOpacity: 0,
            flare: !1,
            duration: 2,
          },
          5: {
            pulseOpacity: [0.6, 0.95],
            pulseScale: [0.8, 1.25],
            centerOpacity: 1,
            ringOneOpacity: 0.5,
            ringTwoOpacity: 0.3,
            ringThreeOpacity: 0,
            tracesOpacity: 0,
            flare: !1,
            duration: 1.8,
          },
          6: {
            pulseOpacity: [0.7, 1],
            pulseScale: [0.75, 1.3],
            centerOpacity: 1,
            ringOneOpacity: 0.6,
            ringTwoOpacity: 0.4,
            ringThreeOpacity: 0,
            tracesOpacity: 0,
            flare: !1,
            duration: 1.6,
          },
          7: {
            pulseOpacity: [0.7, 1],
            pulseScale: [0.7, 1.35],
            centerOpacity: 1,
            ringOneOpacity: 0.7,
            ringTwoOpacity: 0.5,
            ringThreeOpacity: 0.2,
            tracesOpacity: 0,
            flare: !1,
            duration: 1.4,
          },
          8: {
            pulseOpacity: [0.75, 1],
            pulseScale: [0.65, 1.4],
            centerOpacity: 1,
            ringOneOpacity: 0.8,
            ringTwoOpacity: 0.6,
            ringThreeOpacity: 0.3,
            tracesOpacity: 0.4,
            flare: !1,
            duration: 1.2,
          },
          9: {
            pulseOpacity: [0.8, 1],
            pulseScale: [0.6, 1.45],
            centerOpacity: 1,
            ringOneOpacity: 1,
            ringTwoOpacity: 0.7,
            ringThreeOpacity: 0.4,
            tracesOpacity: 0.6,
            flare: !0,
            duration: 0.9,
          },
          10: {
            pulseOpacity: [0.85, 1],
            pulseScale: [0.55, 1.5],
            centerOpacity: 1,
            ringOneOpacity: 1,
            ringTwoOpacity: 0.8,
            ringThreeOpacity: 0.5,
            tracesOpacity: 0.8,
            flare: !0,
            duration: 0.8,
          },
          11: {
            pulseOpacity: [0.9, 1],
            pulseScale: [0.5, 1.55],
            centerOpacity: 1,
            ringOneOpacity: 1,
            ringTwoOpacity: 0.9,
            ringThreeOpacity: 0.6,
            tracesOpacity: 0.9,
            flare: !0,
            duration: 0.7,
          },
          12: {
            pulseOpacity: [0.95, 1],
            pulseScale: [0.45, 1.6],
            centerOpacity: 1,
            ringOneOpacity: 1,
            ringTwoOpacity: 1,
            ringThreeOpacity: 0.7,
            tracesOpacity: 1,
            flare: !0,
            duration: 0.6,
          },
        }[Math.min(Math.max(i, 1), 12)];
      return (0, t.jsx)("div", {
        className:
          "relative flex items-center justify-center pointer-events-none",
        style: { width: s, height: s },
        children: (0, t.jsxs)("svg", {
          viewBox: "0 0 100 100",
          className: "w-full h-full overflow-visible",
          "aria-hidden": "true",
          focusable: "false",
          children: [
            (0, t.jsx)("circle", {
              cx: "50",
              cy: "50",
              r: "16",
              fill: a,
              className: l ? "" : "animate-chakra-pulse",
              style: {
                opacity: l ? 0.16 : 0.22,
                transform: "translateZ(0)",
                transformOrigin: "50% 50%",
                "--pulse-duration": `${n.duration}s`,
                "--pulse-opacity-min": 0.18 * n.pulseOpacity[0],
                "--pulse-opacity-max": 0.24 * n.pulseOpacity[1],
                "--pulse-scale-min": n.pulseScale[0],
                "--pulse-scale-max": n.pulseScale[1],
              },
            }),
            (0, t.jsx)("circle", {
              cx: "50",
              cy: "50",
              r: "10",
              fill: a,
              className: l ? "" : "animate-chakra-pulse",
              style: {
                willChange: l ? "auto" : "transform",
                transform: "translateZ(0)",
                opacity: l ? 0.8 : 0.5,
                "--pulse-duration": `${n.duration}s`,
                "--pulse-opacity-min": n.pulseOpacity[0],
                "--pulse-opacity-max": n.pulseOpacity[1],
                "--pulse-scale-min": n.pulseScale[0],
                "--pulse-scale-max": n.pulseScale[1],
              },
            }),
            (0, t.jsx)("circle", {
              cx: "50",
              cy: "50",
              r: "4",
              fill: "var(--color-light-50)",
              opacity: n.centerOpacity,
            }),
            (0, t.jsx)("circle", {
              cx: "50",
              cy: "50",
              r: "18",
              stroke: a,
              strokeWidth: "1",
              fill: "none",
              strokeDasharray: "10 15",
              opacity: n.ringOneOpacity,
              className: l ? "" : "animate-chakra-spin-cw",
              style: {
                transformOrigin: "center",
                willChange: l ? "auto" : "transform",
                transform: "translateZ(0)",
                "--spin-duration": "12s",
              },
            }),
            i >= 4 &&
              (0, t.jsx)("circle", {
                cx: "50",
                cy: "50",
                r: "28",
                stroke: a,
                strokeWidth: "1.5",
                fill: "none",
                strokeDasharray: "4 12",
                opacity: n.ringTwoOpacity,
                className: l ? "" : "animate-chakra-spin-ccw",
                style: {
                  transformOrigin: "center",
                  willChange: l ? "auto" : "transform",
                  transform: "translateZ(0)",
                  "--spin-duration": "8s",
                },
              }),
            i >= 8 &&
              (0, t.jsx)("circle", {
                cx: "50",
                cy: "50",
                r: "38",
                stroke: a,
                strokeWidth: "0.5",
                fill: "none",
                strokeDasharray: "2 18",
                opacity: n.ringThreeOpacity,
                className: l ? "" : "animate-chakra-spin-cw",
                style: {
                  transformOrigin: "center",
                  willChange: l ? "auto" : "transform",
                  transform: "translateZ(0)",
                  "--spin-duration": "15s",
                },
              }),
            !l &&
              i >= 8 &&
              (0, t.jsxs)("g", {
                className: "animate-chakra-flicker",
                style: {
                  opacity: n.tracesOpacity,
                  willChange: "opacity, transform",
                  transform: "translateZ(0)",
                  "--flicker-duration": r ? "0.6s" : "1.5s",
                },
                children: [
                  (0, t.jsx)("line", {
                    x1: "10",
                    y1: "50",
                    x2: "30",
                    y2: "50",
                    stroke: a,
                    strokeWidth: "1.5",
                    opacity: "0.5",
                  }),
                  (0, t.jsx)("line", {
                    x1: "70",
                    y1: "50",
                    x2: "90",
                    y2: "50",
                    stroke: a,
                    strokeWidth: "1.5",
                    opacity: "0.5",
                  }),
                  (0, t.jsx)("line", {
                    x1: "50",
                    y1: "10",
                    x2: "50",
                    y2: "30",
                    stroke: a,
                    strokeWidth: "1.5",
                    opacity: "0.5",
                  }),
                  (0, t.jsx)("line", {
                    x1: "50",
                    y1: "70",
                    x2: "50",
                    y2: "90",
                    stroke: a,
                    strokeWidth: "1.5",
                    opacity: "0.5",
                  }),
                ],
              }),
            !l &&
              n.flare &&
              (0, t.jsx)("path", {
                d: "M 50 15 L 50 5 L 60 5 L 60 15 M 50 85 L 50 95 L 40 95 L 40 85",
                stroke: a,
                strokeWidth: "1",
                fill: "none",
                className: "animate-chakra-flare",
              }),
          ],
        }),
      });
    }
    function S({ level: e, color: a }) {
      let s = Array.from({ length: 3 }, (t, a) => {
          let s = Math.max(0, Math.min(4, e - 4 * a));
          return { filled: s > 0, strength: s / 4 };
        }),
        r = ["alpha", "beta", "omega"],
        l = "polygon(10% 0%, 100% 0%, 100% 70%, 90% 100%, 0% 100%, 0% 30%)";
      return (0, t.jsx)("div", {
        className: "flex items-center gap-1 mt-1",
        "aria-hidden": "true",
        children: s.map((e, s) => {
          let i = e.filled ? 0.35 + 0.45 * e.strength : 0.12,
            n = e.filled ? 0.12 + 0.3 * e.strength : 0;
          return (0, t.jsxs)(
            "div",
            {
              className: "relative h-2.5 w-5.5 overflow-hidden border",
              style: {
                clipPath: l,
                borderColor: e.filled
                  ? `${a}${Math.round(255 * i)
                      .toString(16)
                      .padStart(2, "0")}`
                  : "rgba(255,255,255,0.12)",
                backgroundColor: e.filled
                  ? `${a}${Math.round(255 * n)
                      .toString(16)
                      .padStart(2, "0")}`
                  : "rgba(255,255,255,0.03)",
              },
              children: [
                (0, t.jsx)("div", {
                  className:
                    "pointer-events-none absolute inset-[-2px] opacity-0 transition-opacity duration-500",
                  style: {
                    background: `linear-gradient(90deg, transparent, ${a}55, transparent)`,
                    opacity: e.filled ? Math.min(0.52, 0.48 * e.strength) : 0,
                  },
                }),
                (0, t.jsx)("div", {
                  className:
                    "absolute inset-y-0 left-0 w-full origin-left transition-[opacity,transform] duration-500",
                  style: {
                    background: `linear-gradient(90deg, ${a}55, ${a})`,
                    opacity: 0.95 * !!e.filled,
                    transform: `scaleX(${e.strength})`,
                    clipPath: l,
                  },
                }),
                (0, t.jsx)("div", {
                  className: "absolute inset-0 opacity-20",
                  children: (0, t.jsx)("div", {
                    className:
                      "absolute left-1 right-1 top-[2px] h-px bg-light-50/20",
                  }),
                }),
              ],
            },
            `${a}-${r[s]}`
          );
        }),
      });
    }
    let N = [0, 0.3, 0.5, 0.75, 1],
      O = (0, d.memo)(function ({
        activeSkill: e,
        isOpen: a,
        onClose: s,
        selectedSkill: r,
      }) {
        let l,
          [i, n] = (0, d.useState)(!0),
          [o, c] = (0, d.useState)(!0),
          u = (0, d.useRef)(null),
          p = (0, d.useRef)(null),
          m = (0, d.useRef)(null),
          h = (0, d.useId)();
        (0, d.useEffect)(() => {
          let e = () => {
            n((0, f.shouldUseLiteMobileExperience)()),
              c((0, f.shouldUseFullscreenSheet)());
          };
          return e(), (0, f.subscribeToCapabilityChanges)(e);
        }, []),
          (0, g.useScrollLock)(a, {
            allowScrollWithin: ".react-modal-sheet-container",
            hideScrollbar: !0,
            lockId: "chakra-skills-sheet-lock",
          }),
          (0, b.useSheetScrollContainment)(m, a),
          (0, y.useOverlayBackgroundInert)(a),
          (0, d.useEffect)(() => {
            if (!a) {
              let e = p.current;
              e?.isConnected && window.requestAnimationFrame(() => e.focus());
              return;
            }
            p.current =
              document.activeElement instanceof HTMLElement
                ? document.activeElement
                : null;
            let e = window.requestAnimationFrame(() => {
              u.current?.focus({ preventScroll: !0 });
            });
            return () => window.cancelAnimationFrame(e);
          }, [a]),
          (0, d.useEffect)(() => {
            if (!a) return;
            let e = (e) => {
              let t;
              if ("Escape" === e.key) {
                e.preventDefault(), s();
                return;
              }
              if ("Tab" !== e.key) return;
              let a = (t = u.current)
                ? Array.from(
                    t.querySelectorAll(
                      'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
                    )
                  ).filter(
                    (e) =>
                      !e.hasAttribute("disabled") &&
                      "true" !== e.getAttribute("aria-hidden") &&
                      e.getClientRects().length > 0
                  )
                : [];
              if (0 === a.length) {
                e.preventDefault(), u.current?.focus({ preventScroll: !0 });
                return;
              }
              let r = a[0],
                l = a[a.length - 1],
                i =
                  document.activeElement instanceof HTMLElement
                    ? document.activeElement
                    : null;
              if (!i || !u.current?.contains(i)) {
                e.preventDefault(), r.focus();
                return;
              }
              if (e.shiftKey && i === r) {
                e.preventDefault(), l.focus();
                return;
              }
              e.shiftKey || i !== l || (e.preventDefault(), r.focus());
            };
            return (
              window.addEventListener("keydown", e),
              () => window.removeEventListener("keydown", e)
            );
          }, [a, s]);
        let O = e ? k(e.mastery) : 0,
          T = e ? w(e.mastery) : "",
          C = o ? "0px" : "24px";
        return (0, t.jsxs)(x.Sheet, {
          disableScrollLocking: !0,
          isOpen: a,
          onClose: s,
          onOpenEnd: () => {
            u.current?.focus({ preventScroll: !0 });
          },
          detent: "full",
          snapPoints: [...N],
          initialSnap: b.DEFAULT_SHEET_SNAP_INDEX,
          children: [
            (0, t.jsxs)(x.Sheet.Container, {
              ref: u,
              role: "dialog",
              "aria-modal": "true",
              "aria-labelledby": h,
              tabIndex: -1,
              className: (0, v.cn)(
                "flex w-full flex-col focus:outline-none",
                o
                  ? "max-w-none"
                  : "mx-auto max-w-lg md:max-w-xl lg:max-w-[52rem]"
              ),
              style: {
                backgroundColor: b.SHEET_SURFACE.skills,
                borderTopLeftRadius: C,
                borderTopRightRadius: C,
                overflow: "hidden",
                right: 0,
              },
              children: [
                (0, t.jsx)(x.Sheet.Header, {
                  style: {
                    background: (0, b.getSheetHeaderGradient)(
                      b.SHEET_SURFACE.skills,
                      "#000000"
                    ),
                    borderTopLeftRadius: C,
                    borderTopRightRadius: C,
                    overflow: "hidden",
                  },
                  children:
                    e &&
                    null !== r &&
                    (0, t.jsxs)("div", {
                      className:
                        "relative overflow-hidden px-5 pb-5 pt-3 font-mono",
                      children: [
                        (0, t.jsx)("div", {
                          className: "relative z-10 mb-4 flex justify-center",
                          children: (0, t.jsx)(x.Sheet.DragIndicator, {}),
                        }),
                        !i &&
                          (0, t.jsxs)(t.Fragment, {
                            children: [
                              (0, t.jsx)("div", {
                                className:
                                  "pointer-events-none absolute -right-14 -top-24 h-56 w-56 rounded-full opacity-20 blur-3xl",
                                style: { backgroundColor: e.color },
                              }),
                              (0, t.jsx)("div", {
                                className:
                                  "pointer-events-none absolute -left-24 bottom-0 h-40 w-40 rounded-full opacity-10 blur-3xl",
                                style: { backgroundColor: e.color },
                              }),
                            ],
                          }),
                        i &&
                          (0, t.jsx)("div", {
                            className:
                              "pointer-events-none absolute -right-10 -top-16 h-40 w-40 rounded-full opacity-15",
                            style: {
                              background: `radial-gradient(circle, ${e.color}55 0%, transparent 70%)`,
                            },
                          }),
                        (0, t.jsx)("div", {
                          className:
                            "pointer-events-none absolute inset-x-5 bottom-0 h-px",
                          style: {
                            background: `linear-gradient(90deg, transparent, ${e.color}80, transparent)`,
                          },
                        }),
                        (0, t.jsxs)("div", {
                          className: "relative z-10",
                          children: [
                            (0, t.jsxs)("div", {
                              className:
                                "mb-4 flex items-start justify-between gap-4",
                              children: [
                                (0, t.jsxs)("div", {
                                  className: "min-w-0 flex-1",
                                  children: [
                                    (0, t.jsxs)("div", {
                                      className:
                                        "mb-3 flex flex-wrap items-center gap-2",
                                      children: [
                                        (0, t.jsx)("span", {
                                          className:
                                            "rounded-full border px-2.5 py-1 text-[9px] font-black uppercase tracking-[0.22em]",
                                          style: {
                                            color: e.color,
                                            borderColor: `${e.color}40`,
                                            backgroundColor: `${e.color}12`,
                                          },
                                          children: e.category,
                                        }),
                                        (0, t.jsxs)("span", {
                                          className:
                                            "text-[9px] font-bold uppercase tracking-[0.24em] text-foreground/35",
                                          children: [
                                            "Entry 0x",
                                            r.toString(16).padStart(2, "0"),
                                          ],
                                        }),
                                      ],
                                    }),
                                    (0, t.jsx)("h2", {
                                      id: h,
                                      className:
                                        "text-[2.05rem] font-black uppercase leading-[0.92] tracking-normal text-foreground",
                                      style: i
                                        ? void 0
                                        : {
                                            textShadow: `0 0 24px ${e.color}35`,
                                          },
                                      children: e.name,
                                    }),
                                    (0, t.jsx)("p", {
                                      className:
                                        "mt-3 text-xs font-black uppercase tracking-[0.18em]",
                                      style: { color: e.color },
                                      children: e.summary,
                                    }),
                                  ],
                                }),
                                (0, t.jsx)("div", {
                                  className:
                                    "flex shrink-0 flex-col items-center pt-1",
                                  children: (0, t.jsx)(j, {
                                    level: O,
                                    color: e.color,
                                    size: 68,
                                    isMaxed: 12 === O,
                                    disableAnimations: i,
                                  }),
                                }),
                              ],
                            }),
                            (0, t.jsxs)("div", {
                              className: "space-y-3",
                              children: [
                                (0, t.jsxs)("div", {
                                  className:
                                    "flex items-end justify-between gap-4",
                                  children: [
                                    (0, t.jsxs)("div", {
                                      children: [
                                        (0, t.jsx)("span", {
                                          className:
                                            "block text-[9px] font-black uppercase tracking-[0.24em] text-foreground/35",
                                          children: "How I Use It",
                                        }),
                                        (0, t.jsx)("span", {
                                          className:
                                            "mt-1 block text-lg font-black uppercase leading-none",
                                          style: { color: e.color },
                                          children: T,
                                        }),
                                      ],
                                    }),
                                    (0, t.jsx)(S, { level: O, color: e.color }),
                                  ],
                                }),
                                (0, t.jsx)("div", {
                                  className:
                                    "h-1.5 overflow-hidden rounded-full bg-light-50/10",
                                  children: (0, t.jsx)("div", {
                                    className:
                                      "h-full w-full origin-left rounded-full",
                                    style: {
                                      background: `linear-gradient(90deg, ${e.color}70, ${e.color})`,
                                      transform: `scaleX(${e.mastery / 100})`,
                                    },
                                  }),
                                }),
                                (0, t.jsxs)("div", {
                                  className:
                                    "flex items-center justify-between text-[9px] font-black uppercase tracking-[0.22em] text-foreground/35",
                                  children: [
                                    (0, t.jsx)("span", { children: e.label }),
                                    (0, t.jsxs)("span", {
                                      children: [e.mastery, "% Sync"],
                                    }),
                                  ],
                                }),
                              ],
                            }),
                          ],
                        }),
                      ],
                    }),
                }),
                (0, t.jsx)(b.CalculatedSheetContent, {
                  scrollerRef: m,
                  disableDrag: !0,
                  style: {
                    backgroundColor: b.SHEET_SURFACE.skills,
                    padding: 0,
                  },
                  scrollClassName: "skills-sheet-scroller",
                  scrollStyle: { ...b.SHEET_SCROLLER_STYLE },
                  children:
                    e &&
                    (0, t.jsx)("div", {
                      className: "px-5 pb-12 pt-5 font-mono",
                      children: (0, t.jsxs)("div", {
                        className: "space-y-7",
                        children: [
                          (0, t.jsxs)("div", {
                            className: "space-y-4",
                            children: [
                              (0, t.jsxs)("div", {
                                className: "border-l-2 py-0.5 pl-4",
                                style: { borderColor: e.color },
                                children: [
                                  (0, t.jsx)("h3", {
                                    className:
                                      "text-[10px] font-black uppercase tracking-[0.24em] text-foreground/40",
                                    children: "Field Note",
                                  }),
                                  (0, t.jsx)("p", {
                                    className:
                                      "mt-2 text-sm font-semibold leading-relaxed text-foreground/72",
                                    children:
                                      (l = k(e.mastery)) >= 9
                                        ? "I use this daily."
                                        : l >= 6
                                        ? "Comfortable here, still learning the edges."
                                        : "Solid basics, more range to go.",
                                  }),
                                ],
                              }),
                              (0, t.jsxs)("div", {
                                children: [
                                  (0, t.jsxs)("h3", {
                                    className:
                                      "mb-2 flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.24em] text-foreground/40",
                                    children: [
                                      (0, t.jsx)("span", {
                                        className: "h-1.5 w-1.5 rounded-full",
                                        style: { backgroundColor: e.color },
                                      }),
                                      "Skill Analysis",
                                    ],
                                  }),
                                  (0, t.jsx)("p", {
                                    className:
                                      "text-[15px] font-medium leading-relaxed text-foreground/78",
                                    children: e.description,
                                  }),
                                ],
                              }),
                            ],
                          }),
                          (0, t.jsx)("div", {
                            className:
                              "space-y-3 border-y border-light-200/10 py-5",
                            children: e.details.map((a) =>
                              (0, t.jsxs)(
                                "div",
                                {
                                  className:
                                    "grid grid-cols-[5.5rem_1fr] gap-4",
                                  children: [
                                    (0, t.jsx)("span", {
                                      className:
                                        "text-[10px] font-black uppercase leading-relaxed tracking-[0.18em]",
                                      style: { color: e.color },
                                      children: a.label,
                                    }),
                                    (0, t.jsx)("p", {
                                      className:
                                        "text-sm font-semibold leading-relaxed text-foreground/75",
                                      children: a.value,
                                    }),
                                  ],
                                },
                                a.label
                              )
                            ),
                          }),
                          (0, t.jsxs)("div", {
                            children: [
                              (0, t.jsx)("h3", {
                                className:
                                  "mb-3 text-[10px] font-black uppercase tracking-[0.24em] text-foreground/40",
                                children: "Active Stack",
                              }),
                              (0, t.jsx)("div", {
                                className: "flex flex-wrap gap-2",
                                children: e.tags?.map((a) =>
                                  (0, t.jsx)(
                                    "span",
                                    {
                                      className:
                                        "rounded-full border px-3 py-1.5 text-[10px] font-black uppercase tracking-wider",
                                      style: {
                                        color: e.color,
                                        borderColor: `${e.color}36`,
                                        backgroundColor: `${e.color}10`,
                                      },
                                      children: a,
                                    },
                                    a
                                  )
                                ),
                              }),
                            ],
                          }),
                          (0, t.jsxs)("div", {
                            className:
                              "flex justify-between pt-1 text-[9px] font-black uppercase tracking-[0.28em] text-foreground/30",
                            children: [
                              (0, t.jsx)("span", { children: "Core Stable" }),
                              (0, t.jsx)("span", { children: "Module Active" }),
                            ],
                          }),
                        ],
                      }),
                    }),
                }),
              ],
            }),
            (0, t.jsx)(x.Sheet.Backdrop, {
              onTap: s,
              style: { backgroundColor: "rgba(0, 0, 0, 0.7)" },
            }),
          ],
        });
      });
    var T = e.i(36133);
    function C({ swiper: e, extendParams: t, emit: a, once: s }) {
      t({
        freeMode: {
          enabled: !1,
          momentum: !0,
          momentumRatio: 1,
          momentumBounce: !0,
          momentumBounceRatio: 1,
          momentumVelocityRatio: 1,
          sticky: !1,
          minimumVelocity: 0.02,
        },
      }),
        Object.assign(e, {
          freeMode: {
            onTouchStart: function () {
              if (e.params.cssMode) return;
              let t = e.getTranslate();
              e.setTranslate(t),
                e.setTransition(0),
                (e.touchEventsData.velocities.length = 0),
                e.freeMode.onTouchEnd({
                  currentPos: e.rtl ? e.translate : -e.translate,
                });
            },
            onTouchMove: function () {
              if (e.params.cssMode) return;
              let { touchEventsData: t, touches: a } = e;
              0 === t.velocities.length &&
                t.velocities.push({
                  position: a[e.isHorizontal() ? "startX" : "startY"],
                  time: t.touchStartTime,
                }),
                t.velocities.push({
                  position: a[e.isHorizontal() ? "currentX" : "currentY"],
                  time: (0, T.h)(),
                });
            },
            onTouchEnd: function ({ currentPos: t }) {
              if (e.params.cssMode) return;
              let {
                  params: r,
                  wrapperEl: l,
                  rtlTranslate: i,
                  snapGrid: n,
                  touchEventsData: o,
                } = e,
                c = (0, T.h)() - o.touchStartTime;
              if (t < -e.minTranslate()) return void e.slideTo(e.activeIndex);
              if (t > -e.maxTranslate())
                return void (e.slides.length < n.length
                  ? e.slideTo(n.length - 1)
                  : e.slideTo(e.slides.length - 1));
              if (r.freeMode.momentum) {
                let t, c;
                if (o.velocities.length > 1) {
                  let t = o.velocities.pop(),
                    a = o.velocities.pop(),
                    s = t.position - a.position,
                    l = t.time - a.time;
                  (e.velocity = s / l),
                    (e.velocity /= 2),
                    Math.abs(e.velocity) < r.freeMode.minimumVelocity &&
                      (e.velocity = 0),
                    (l > 150 || (0, T.h)() - t.time > 300) && (e.velocity = 0);
                } else e.velocity = 0;
                (e.velocity *= r.freeMode.momentumVelocityRatio),
                  (o.velocities.length = 0);
                let d = 1e3 * r.freeMode.momentumRatio,
                  u = e.velocity * d,
                  p = e.translate + u;
                i && (p = -p);
                let m = !1,
                  h =
                    20 * Math.abs(e.velocity) * r.freeMode.momentumBounceRatio;
                if (p < e.maxTranslate())
                  r.freeMode.momentumBounce
                    ? (p + e.maxTranslate() < -h && (p = e.maxTranslate() - h),
                      (t = e.maxTranslate()),
                      (m = !0),
                      (o.allowMomentumBounce = !0))
                    : (p = e.maxTranslate()),
                    r.loop && r.centeredSlides && (c = !0);
                else if (p > e.minTranslate())
                  r.freeMode.momentumBounce
                    ? (p - e.minTranslate() > h && (p = e.minTranslate() + h),
                      (t = e.minTranslate()),
                      (m = !0),
                      (o.allowMomentumBounce = !0))
                    : (p = e.minTranslate()),
                    r.loop && r.centeredSlides && (c = !0);
                else if (r.freeMode.sticky) {
                  let t;
                  for (let e = 0; e < n.length; e += 1)
                    if (n[e] > -p) {
                      t = e;
                      break;
                    }
                  p = -(p =
                    Math.abs(n[t] - p) < Math.abs(n[t - 1] - p) ||
                    "next" === e.swipeDirection
                      ? n[t]
                      : n[t - 1]);
                }
                if (
                  (c &&
                    s("transitionEnd", () => {
                      e.loopFix();
                    }),
                  0 !== e.velocity)
                ) {
                  if (
                    ((d = i
                      ? Math.abs((-p - e.translate) / e.velocity)
                      : Math.abs((p - e.translate) / e.velocity)),
                    r.freeMode.sticky)
                  ) {
                    let t = Math.abs((i ? -p : p) - e.translate),
                      a = e.slidesSizesGrid[e.activeIndex];
                    d =
                      t < a
                        ? r.speed
                        : t < 2 * a
                        ? 1.5 * r.speed
                        : 2.5 * r.speed;
                  }
                } else if (r.freeMode.sticky) return void e.slideToClosest();
                r.freeMode.momentumBounce && m
                  ? (e.updateProgress(t),
                    e.setTransition(d),
                    e.setTranslate(p),
                    e.transitionStart(!0, e.swipeDirection),
                    (e.animating = !0),
                    (0, T.o)(l, () => {
                      e &&
                        !e.destroyed &&
                        o.allowMomentumBounce &&
                        (a("momentumBounce"),
                        e.setTransition(r.speed),
                        setTimeout(() => {
                          e.setTranslate(t),
                            (0, T.o)(l, () => {
                              e && !e.destroyed && e.transitionEnd();
                            });
                        }, 0));
                    }))
                  : e.velocity
                  ? (a("_freeModeNoMomentumRelease"),
                    e.updateProgress(p),
                    e.setTransition(d),
                    e.setTranslate(p),
                    e.transitionStart(!0, e.swipeDirection),
                    e.animating ||
                      ((e.animating = !0),
                      (0, T.o)(l, () => {
                        e && !e.destroyed && e.transitionEnd();
                      })))
                  : e.updateProgress(p),
                  e.updateActiveIndex(),
                  e.updateSlidesClasses();
              } else {
                if (r.freeMode.sticky) return void e.slideToClosest();
                r.freeMode && a("_freeModeNoMomentumRelease");
              }
              (!r.freeMode.momentum || c >= r.longSwipesMs) &&
                (a("_freeModeStaticRelease"),
                e.updateProgress(),
                e.updateActiveIndex(),
                e.updateSlidesClasses());
            },
          },
        });
    }
    var M = e.i(589320);
    let $ = () =>
        window.innerWidth <= 768 ||
        window.matchMedia("(pointer: coarse)").matches ||
        (0, f.shouldUseLowEndRenderMode)(),
      E = [2, 4, 1, 5, 3],
      R = [
        {
          name: "Creative Development",
          category: "CREATIVE",
          tags: [
            "Three.js",
            "React Three Fiber",
            "TresJS",
            "WebGL",
            "GLSL",
            "Shaders",
            "Creative Coding",
            "Art Direction",
          ],
          color: "#c57cff",
          position: { x: 49.85, y: 22.23 },
          description:
            "The part where an idea stops being a mockup and becomes something you can move through. I am not a shader specialist, but I know enough 3D to build the thing and enough frontend to keep it fast.",
          summary: "3D, motion, and ideas that need both",
          label: "Sahasrara",
          logoPlacement: "right",
          yOffset: 0,
          mastery: 58,
          details: [
            {
              label: "Best For",
              value:
                "creative sites, interactive storytelling, launch pages meant to be remembered",
            },
            {
              label: "Strong With",
              value:
                "3D scenes with React Three Fiber, art direction, knowing when 3D is the wrong answer",
            },
            {
              label: "Tools",
              value: "Three.js, React Three Fiber, TresJS, WebGL, GLSL",
            },
            {
              label: "Proven On",
              value:
                "This site: WebGL avatar, portal scene, custom dissolve shaders",
            },
          ],
        },
        {
          name: "Accessibility & SEO",
          category: "CODE",
          tags: [
            "WCAG",
            "ARIA",
            "Keyboard Nav",
            "Screen Readers",
            "Focus Management",
            "react-i18next",
            "Structured Data",
            "Meta & Open Graph",
          ],
          color: "#5197f7",
          position: { x: 49.85, y: 27.4 },
          description:
            "Two audiences never see the screen: assistive technology and search crawlers. Both read the same markup, and both punish you for exactly the same shortcuts.",
          summary: "Usable by everyone, findable by search",
          label: "Ajna",
          logoPlacement: "left",
          yOffset: 0,
          mastery: 73,
          details: [
            {
              label: "Best For",
              value:
                "public sector and regulated work, content that has to rank, products with compliance requirements",
            },
            {
              label: "Strong With",
              value:
                "keyboard paths, focus order, reduced-motion fallbacks, crawlable structure and metadata",
            },
            {
              label: "Tools",
              value:
                "Lighthouse, axe DevTools, screen readers, JSON-LD, react-i18next",
            },
            {
              label: "Proven On",
              value:
                "This site: reduced-motion fallbacks, focus management, per-page metadata and a live sitemap",
            },
          ],
        },
        {
          name: "Interface Design",
          category: "DESIGN",
          tags: [
            "Figma",
            "Photoshop",
            "Wireframes",
            "Prototyping",
            "Design Tokens",
            "Type Scales",
            "Color Systems",
            "Visual Hierarchy",
          ],
          color: "#14b8a6",
          position: { x: 49.85, y: 34.2 },
          description:
            "Deciding what a screen is actually saying before a single component is built. Hierarchy first, then the details that make it feel finished.",
          summary: "Hierarchy, type, and the pass before code",
          label: "Vishuddha",
          logoPlacement: "right",
          yOffset: 0,
          mastery: 78,
          details: [
            {
              label: "Best For",
              value:
                "interface direction, wireframes, giving a product its visual voice",
            },
            {
              label: "Strong With",
              value:
                "layout and hierarchy, type scales, color systems with rules",
            },
            { label: "Tools", value: "Figma, Photoshop, design tokens" },
            {
              label: "Proven On",
              value:
                "Dubai Worx: a dashboard people sit inside for a full shift",
            },
          ],
        },
        {
          name: "Design Systems",
          category: "DESIGN",
          tags: [
            "Tailwind CSS",
            "UnoCSS",
            "SCSS",
            "BEM",
            "Storybook",
            "shadcn/ui",
            "Radix",
            "Vuetify",
          ],
          color: "#68e468",
          position: { x: 49.8, y: 43.1 },
          description:
            "One button, used four hundred times, in a codebase several people are editing. Systems work is mostly about the decisions you never have to make twice.",
          summary: "Components that hold up at scale",
          label: "Anahata",
          logoPlacement: "left",
          yOffset: 0,
          mastery: 73,
          details: [
            {
              label: "Best For",
              value:
                "design systems, shared component libraries, multi-team frontends",
            },
            {
              label: "Strong With",
              value:
                "component APIs, token architecture, styling that stays sane",
            },
            {
              label: "Tools",
              value:
                "Tailwind CSS, UnoCSS, SCSS, Storybook, shadcn/ui, Radix, Vuetify, PrimeVue",
            },
            {
              label: "Proven On",
              value: "Build in Dubai: shared components across 60+ services",
            },
          ],
        },
        {
          name: "Frontend Architecture",
          category: "CODE",
          tags: [
            "React",
            "Vue.js",
            "Next.js",
            "Nuxt.js",
            "TypeScript",
            "Pinia",
            "React Query",
            "Zustand",
          ],
          color: "#ffe040",
          position: { x: 49.75, y: 51.9 },
          description:
            "The structure under the surface: how state moves, how data arrives, and how a codebase survives four years of new requirements. This is the part I lead.",
          summary: "Vue and React at platform scale",
          label: "Manipura",
          logoPlacement: "right",
          yOffset: 0,
          mastery: 87,
          details: [
            {
              label: "Best For",
              value:
                "large platforms, long-lived codebases, teams that need one structure",
            },
            {
              label: "Strong With",
              value:
                "app architecture in both ecosystems, typed state and data flow, SSR and routing",
            },
            {
              label: "Tools",
              value:
                "React and Hooks, Vue.js and the Composition API, Next.js, Nuxt.js, TypeScript, Pinia, React Query, Zustand",
            },
            {
              label: "Proven On",
              value:
                "Build in Dubai: the architecture behind 60+ government services",
            },
          ],
        },
        {
          name: "Interactivity & Motion",
          category: "CREATIVE",
          tags: [
            "GSAP",
            "ScrollTrigger",
            "Motion",
            "Interactive Animation",
            "Easing & Timing",
            "Scroll Sequences",
            "Micro-interactions",
            "Transitions",
          ],
          color: "#f3651b",
          position: { x: 49.5, y: 60.9 },
          description:
            "Motion is feedback. Good timing tells you that something happened, where it came from, and where you are now, without a single word of copy.",
          summary: "Timing, feedback, and how it feels",
          label: "Svadhisthana",
          logoPlacement: "left",
          yOffset: 0,
          mastery: 75,
          details: [
            {
              label: "Best For",
              value:
                "micro-interactions, section transitions, interfaces that feel alive",
            },
            {
              label: "Strong With",
              value:
                "timing and easing, scroll-driven sequences, interaction feedback",
            },
            { label: "Tools", value: "GSAP, ScrollTrigger, Motion" },
            {
              label: "Proven On",
              value:
                "Every transition on this site, including the one you just scrolled",
            },
          ],
        },
        {
          name: "Web Foundation",
          category: "CODE",
          tags: [
            "HTML",
            "CSS",
            "JavaScript (ES6)",
            "Semantics",
            "Flexbox & Grid",
            "Responsive",
            "Cross-browser",
            "Progressive Enhancement",
          ],
          color: "#d61d23",
          position: { x: 49.6, y: 69.1 },
          description:
            "The unglamorous half that decides whether the rest of it works. Real markup, modern layout, and pages that hold their shape from 320px to an ultrawide.",
          summary: "Semantics, accessibility, responsive",
          label: "Muladhara",
          logoPlacement: "right",
          yOffset: 0,
          mastery: 84,
          details: [
            {
              label: "Best For",
              value:
                "responsive layouts, semantic structure, accessible frontend work",
            },
            {
              label: "Strong With",
              value:
                "HTML semantics, Grid and Flexbox layout, fluid type and spacing",
            },
            {
              label: "Tools",
              value: "HTML, CSS, JavaScript, browser DevTools",
            },
            {
              label: "Proven On",
              value: "Eight years, every project on this page",
            },
          ],
        },
      ],
      A = (0, d.memo)(({ skill: e, index: a, onClick: s }) => {
        let l = (0, d.useRef)(null),
          i = E[a % E.length];
        return (0, t.jsx)("div", {
          ref: l,
          "data-scroll-reveal-card": !0,
          className: "w-full",
          children: (0, t.jsx)("button", {
            type: "button",
            onClick: () => s(a),
            className:
              "group w-full text-left focus:outline-none focus-visible:ring-2 focus-visible:ring-primary-300/75 focus-visible:ring-offset-2 focus-visible:ring-offset-black",
            children: (0, t.jsx)(p.CyberCard, {
              shape: i,
              lean: !0,
              glowColor: e.color,
              className:
                "min-h-[118px] p-3.5 xs:min-h-[112px] xs:p-3 sm:min-h-0 sm:p-4",
              containerClassName: "w-full",
              backgroundColor: "rgba(10, 10, 10, 0.92)",
              isStatic: !0,
              children: (0, t.jsxs)("div", {
                className: "flex items-center gap-4",
                children: [
                  (0, t.jsxs)("div", {
                    className: "flex-shrink-0 relative",
                    children: [
                      (0, t.jsx)("div", {
                        className:
                          "absolute inset-0 rounded-full opacity-30 pointer-events-none",
                        style: {
                          background: `radial-gradient(circle, ${e.color} 0%, transparent 65%)`,
                        },
                      }),
                      (0, t.jsx)(j, {
                        level: k(e.mastery),
                        color: e.color,
                        size: 56,
                        disableAnimations: !0,
                      }),
                    ],
                  }),
                  (0, t.jsxs)("div", {
                    className: "flex-grow min-w-0",
                    children: [
                      (0, t.jsxs)("div", {
                        className: "flex justify-between items-start mb-1",
                        children: [
                          (0, t.jsx)("h4", {
                            className:
                              "text-lg xs:text-base font-black uppercase tracking-tight leading-tight pr-2",
                            style: {
                              color: e.color,
                              textShadow: `0 0 10px ${e.color}40`,
                            },
                            children: e.name,
                          }),
                          (0, t.jsx)("div", {
                            className:
                              "text-[8px] font-bold px-1.5 py-0.5 rounded border flex-shrink-0",
                            style: {
                              color: e.color,
                              borderColor: `${e.color}40`,
                              backgroundColor: `${e.color}10`,
                            },
                            children: "SYNCED",
                          }),
                        ],
                      }),
                      (0, t.jsx)("p", {
                        className:
                          "text-[10px] text-foreground/50 uppercase tracking-widest font-bold mb-2 truncate",
                        children: e.summary,
                      }),
                      (0, t.jsxs)("div", {
                        className: "flex items-center justify-between",
                        children: [
                          (0, t.jsx)(S, {
                            level: k(e.mastery),
                            color: e.color,
                          }),
                          (0, t.jsx)("span", {
                            className:
                              "text-[9px] font-black uppercase tracking-wider opacity-60",
                            style: { color: e.color },
                            children: w(e.mastery),
                          }),
                        ],
                      }),
                    ],
                  }),
                  (0, t.jsx)("div", {
                    className:
                      "flex-shrink-0 opacity-30 group-hover:opacity-100 transition-opacity",
                    children: (0, t.jsx)(r.ChevronRight, {
                      size: 16,
                      style: { color: e.color },
                    }),
                  }),
                ],
              }),
            }),
          }),
        });
      });
    A.displayName = "SkillAppCard";
    let P = ({ onSkillClick: e, skills: r }) => {
        let c = (0, d.useRef)(null),
          u = (0, d.useRef)(null),
          p = (0, d.useRef)(null),
          m = (0, d.useRef)(!1),
          h = (0, d.useRef)(!1),
          [f, x] = (0, d.useState)("ALL"),
          y = (0, d.useMemo)(
            () =>
              "ALL" === f
                ? r.map((e, t) => ({ ...e, originalIndex: t }))
                : r
                    .map((e, t) => ({ ...e, originalIndex: t }))
                    .filter((e) => e.category === f),
            [f, r]
          ),
          g = [
            {
              id: "ALL",
              label: "Neural_All",
              icon: (0, t.jsx)(o.Zap, { size: 14 }),
            },
            {
              id: "CODE",
              label: "Logic_Core",
              icon: (0, t.jsx)(l.Cpu, { size: 14 }),
            },
            {
              id: "DESIGN",
              label: "Vision_UI",
              icon: (0, t.jsx)(i, { size: 14 }),
            },
            {
              id: "CREATIVE",
              label: "Art_Nexus",
              icon: (0, t.jsx)(n.Sparkles, { size: 14 }),
            },
          ];
        return (
          (0, d.useLayoutEffect)(() => {
            let e = p.current;
            if (!e) return;
            let t = Array.from(e.querySelectorAll("[data-skill-mobile-card]"));
            if (0 === t.length) return;
            if (
              (a.gsap.registerPlugin(s.ScrollTrigger),
              a.gsap.killTweensOf(t),
              window.matchMedia("(prefers-reduced-motion: reduce)").matches)
            ) {
              (h.current = !0),
                a.gsap.set(t, {
                  autoAlpha: 1,
                  y: 0,
                  scale: 1,
                  clearProps: "opacity,visibility,transform,willChange",
                });
              return;
            }
            a.gsap.set(t, {
              autoAlpha: 0,
              y: 34,
              scale: 0.982,
              transformOrigin: "50% 100%",
              willChange: "transform,opacity",
            });
            let r = a.gsap.timeline({
              paused: !0,
              defaults: { overwrite: "auto", force3D: !0 },
              onComplete: () => {
                a.gsap.set(t, { clearProps: "willChange" });
              },
            });
            r.to(t, {
              autoAlpha: 1,
              y: 0,
              scale: 1,
              duration: 0.9,
              ease: "power2.out",
              stagger: { each: 0.075, from: "start" },
            });
            let l = !1,
              i = () => {
                l || ((l = !0), (h.current = !0), r.play(0));
              },
              n = () => {
                let t = e.getBoundingClientRect();
                t.top > 0.86 * window.innerHeight || t.bottom < 0 || i();
              },
              o = s.ScrollTrigger.create({
                trigger: e,
                start: "top 86%",
                once: !0,
                invalidateOnRefresh: !0,
                onEnter: i,
                onRefresh: n,
              }),
              c = window.requestAnimationFrame(n);
            return () => {
              window.cancelAnimationFrame(c), o.kill(), r.kill();
            };
          }, []),
          (0, d.useEffect)(() => {
            if (!m.current) {
              m.current = !0;
              return;
            }
            let e = p.current;
            if (
              !e ||
              window.matchMedia("(prefers-reduced-motion: reduce)").matches
            )
              return;
            let t = Array.from(e.querySelectorAll("[data-skill-mobile-card]"));
            if (0 !== t.length) {
              if (!h.current)
                return void a.gsap.set(t, {
                  autoAlpha: 0,
                  y: 34,
                  scale: 0.982,
                  transformOrigin: "50% 100%",
                });
              a.gsap.fromTo(
                t,
                { autoAlpha: 0, y: 20, scale: 0.99 },
                {
                  autoAlpha: 1,
                  y: 0,
                  scale: 1,
                  duration: 0.52,
                  ease: "power2.out",
                  stagger: 0.055,
                  overwrite: "auto",
                  clearProps: "willChange",
                }
              );
            }
          }, [f]),
          (0, t.jsxs)("div", {
            className: "flex flex-col gap-6 w-full max-w-md mx-auto pt-4",
            children: [
              (0, t.jsxs)("div", {
                ref: c,
                "data-mobile-section-block": !0,
                className:
                  "flex justify-between items-end px-2 py-4 border-b border-light-200/5",
                children: [
                  (0, t.jsxs)("div", {
                    className: "flex flex-col",
                    children: [
                      (0, t.jsx)("span", {
                        className:
                          "text-[9px] text-foreground/30 uppercase tracking-[0.3em] font-bold",
                        children: "System_Status",
                      }),
                      (0, t.jsxs)("div", {
                        className: "flex items-center gap-2",
                        children: [
                          (0, t.jsx)("div", {
                            className:
                              "w-1.5 h-1.5 rounded-full bg-primary-500 animate-pulse",
                          }),
                          (0, t.jsx)("span", {
                            className:
                              "text-xs font-mono font-bold text-primary-500/80 uppercase",
                            children: "Neural_Link: Operational",
                          }),
                        ],
                      }),
                    ],
                  }),
                  (0, t.jsxs)("div", {
                    className: "text-right flex flex-col items-end",
                    children: [
                      (0, t.jsx)("span", {
                        className:
                          "text-[9px] text-foreground/30 uppercase tracking-[0.3em] font-bold",
                        children: "Protocol",
                      }),
                      (0, t.jsx)("span", {
                        className:
                          "text-xs font-mono font-bold text-foreground/60",
                        children: "v4.0.2 / ALPHA",
                      }),
                    ],
                  }),
                ],
              }),
              (0, t.jsxs)("div", {
                ref: u,
                "data-mobile-section-block": !0,
                className: "relative z-20 px-2 pb-8",
                children: [
                  (0, t.jsx)(M.Swiper, {
                    slidesPerView: "auto",
                    spaceBetween: 12,
                    freeMode: {
                      enabled: !0,
                      momentum: !0,
                      momentumRatio: 0.8,
                      momentumVelocityRatio: 0.8,
                    },
                    modules: [C],
                    className: "w-full",
                    style: { overflow: "visible" },
                    watchSlidesProgress: !1,
                    roundLengths: !0,
                    threshold: 6,
                    touchEventsTarget: "container",
                    nested: !0,
                    children: g.map((e) =>
                      (0, t.jsx)(
                        M.SwiperSlide,
                        {
                          style: { width: "auto" },
                          children: (0, t.jsxs)(
                            "button",
                            {
                              type: "button",
                              onClick: () => x(e.id),
                              className: `flex items-center gap-2 px-4 xs:px-3 py-2.5 rounded-sm border transition-[background-color,border-color,color,opacity,transform] whitespace-nowrap ${
                                f === e.id
                                  ? "bg-light-50/10 border-light-200/40 text-foreground shadow-[0_0_15px_rgba(255,255,255,0.1)]"
                                  : "bg-transparent border-light-200/5 text-foreground/40 hover:border-light-200/10"
                              }`,
                              children: [
                                e.icon,
                                (0, t.jsx)("span", {
                                  className:
                                    "text-[10px] font-black uppercase tracking-widest",
                                  children: e.label,
                                }),
                              ],
                            },
                            e.id
                          ),
                        },
                        e.id
                      )
                    ),
                  }),
                  (0, t.jsx)("div", {
                    className:
                      "absolute right-0 top-0 bottom-8 w-16 bg-gradient-to-l from-black to-transparent pointer-events-none z-10 opacity-70",
                  }),
                ],
              }),
              (0, t.jsx)("div", {
                ref: p,
                className: "space-y-4 px-1 pb-10",
                children: y.map((a) =>
                  (0, t.jsx)(
                    "div",
                    {
                      "data-skill-mobile-card": !0,
                      style: {
                        opacity: 0,
                        transform: "translateY(34px) scale(0.982)",
                      },
                      children: (0, t.jsx)(A, {
                        skill: a,
                        index: a.originalIndex,
                        onClick: e,
                      }),
                    },
                    a.name
                  )
                ),
              }),
            ],
          })
        );
      },
      L = (0, d.memo)(
        ({
          skill: e,
          index: a,
          isHovered: s,
          onHover: r,
          onLeave: l,
          onClick: i,
          isMobile: n,
          windowWidth: o,
        }) => {
          let c = (0, d.useMemo)(() => {
            let t = s ? 1 : 0.3333333333333333,
              a = {
                backgroundColor: e.color,
                left: `${e.position.x}%`,
                top: `${e.position.y}%`,
                zIndex: 20,
              },
              r = Math.min(Math.max(o, 768), 1536),
              l = (Math.min(r, 1150) - 768) / 382,
              i = r <= 1150 ? 0 : (r - 1150) / 386,
              n = 140 * (1 - l),
              c = 95 * i,
              d = Math.min(Math.max((o - 1900) / 596, 0), 1),
              u = 56 * d,
              p = 400 - n + c + u,
              m = 280 + 42 * i + 32 * d,
              h = -180 + n - c - (m - m),
              f = (s ? p : 350 - n + c + u) / p;
            return {
              chakraPointStyles: a,
              connectingLineStyles: {
                top: `${(e.yOffset || 0) - 6}px`,
                left: "right" === e.logoPlacement ? `${e.position.x}%` : "auto",
                right:
                  "left" === e.logoPlacement
                    ? `${100 - e.position.x}%`
                    : "auto",
                width: `${p}px`,
                height: "12px",
                transformOrigin:
                  "left" === e.logoPlacement ? "right center" : "left center",
                transform: `scaleX(${f}) scaleY(${t})`,
                background: `linear-gradient(to ${
                  "left" === e.logoPlacement ? "left" : "right"
                }, 
                  transparent, ${e.color}80 15%, ${e.color} 50%, ${
                  e.color
                }80 85%, transparent)`,
                "--pulse-travel": `${p - 20}px`,
                zIndex: 15,
                pointerEvents: "none",
              },
              skillLabelStyles: {
                left: "left" === e.logoPlacement ? `${h}px` : "auto",
                right: "right" === e.logoPlacement ? `${h}px` : "auto",
                top: e.yOffset || 0,
                width: `${m}px`,
                zIndex: s ? 50 : 20,
              },
            };
          }, [e, s, o]);
          return (0, t.jsxs)(
            "button",
            {
              type: "button",
              className:
                "relative w-full flex left-0 bg-transparent border-none p-0 pointer-events-auto cursor-pointer",
              style: { zIndex: s ? 100 : 10, top: `${e.position.y}%` },
              onMouseEnter: () => r(a),
              onMouseLeave: l,
              onClick: () => i(a),
              "aria-label": `${e.name} - ${e.description}`,
              onKeyDown: (e) => {
                ("Enter" === e.key || " " === e.key) &&
                  (e.preventDefault(), r(a));
              },
              children: [
                (0, t.jsxs)("div", {
                  className: `chakra-point absolute w-7 h-7 3xl:w-8 3xl:h-8 4xl:w-9 4xl:h-9 rounded-full -translate-x-1/2 -translate-y-1/2 transition-transform cursor-pointer pointer-events-auto focus:outline-none focus:ring-2 focus:ring-primary-500/50 focus:ring-offset-2 focus:ring-offset-black ${
                    s ? "scale-150" : ""
                  }`,
                  style: {
                    ...c.chakraPointStyles,
                    transitionDuration: "300ms",
                    willChange: s ? "transform" : "auto",
                  },
                  "aria-hidden": "true",
                  children: [
                    (0, t.jsx)("div", {
                      className:
                        "pointer-events-none absolute -inset-4 rounded-full opacity-35 transition-[opacity,transform] duration-300",
                      style: {
                        background: `radial-gradient(circle, ${e.color}95 0%, ${e.color}42 34%, transparent 72%)`,
                        opacity: s ? 0.92 : 0.42,
                        transform: s ? "scale(1.28)" : "scale(0.96)",
                      },
                    }),
                    (0, t.jsx)("div", {
                      className:
                        "pointer-events-none absolute -inset-7 rounded-full opacity-0 transition-[opacity,transform] duration-300",
                      style: {
                        background: `radial-gradient(circle, ${e.color}42 0%, ${e.color}18 42%, transparent 74%)`,
                        opacity: s ? 0.5 : 0.12,
                        transform: s ? "scale(1.22)" : "scale(0.78)",
                      },
                    }),
                    (0, t.jsx)("div", {
                      className:
                        "absolute inset-0 flex items-center justify-center",
                      children: (0, t.jsx)("div", {
                        className: `w-2 h-2 rounded-full bg-light-50 transition-transform ${
                          s ? "scale-150" : ""
                        }`,
                        style: { transitionDuration: "300ms" },
                      }),
                    }),
                    (0, t.jsx)("div", {
                      className: "absolute -inset-2 rounded-full border",
                      style: {
                        borderColor: e.color,
                        opacity: s ? 0.25 : 0.15,
                        animation: s
                          ? "subtle-pulse 2s infinite ease-in-out"
                          : "subtle-pulse 3s infinite ease-in-out",
                      },
                    }),
                    (0, t.jsx)("div", {
                      className: "absolute -inset-3 rounded-full border",
                      style: {
                        borderColor: e.color,
                        opacity: s ? 0.15 : 0.1,
                        animation: s
                          ? "subtle-pulse 2.5s infinite ease-in-out 0.5s"
                          : "subtle-pulse 3.5s infinite ease-in-out 0.7s",
                      },
                    }),
                  ],
                }),
                !n &&
                  (0, t.jsxs)("div", {
                    className: "absolute transition-transform",
                    style: {
                      ...c.connectingLineStyles,
                      transitionDuration: "300ms",
                    },
                    children: [
                      (0, t.jsx)("div", {
                        className:
                          "pointer-events-none absolute inset-[-5px_0] opacity-35 transition-opacity duration-300",
                        style: {
                          background: `linear-gradient(to ${
                            "left" === e.logoPlacement ? "left" : "right"
                          }, transparent, ${e.color}30, transparent)`,
                          opacity: s ? 0.84 : 0.32,
                        },
                      }),
                      (0, t.jsx)("div", {
                        className:
                          "pointer-events-none absolute inset-[-10px_0] transition-opacity duration-300",
                        style: {
                          background: `linear-gradient(to ${
                            "left" === e.logoPlacement ? "left" : "right"
                          }, transparent, ${e.color}18 22%, ${e.color}34 50%, ${
                            e.color
                          }18 78%, transparent)`,
                          opacity: s ? 0.78 : 0.24,
                        },
                      }),
                      (0, t.jsxs)("div", {
                        className: `energy-pulse absolute left-0 top-1/2 h-5 w-5 overflow-visible rounded-full transition-opacity ${
                          s ? "opacity-100" : "opacity-70"
                        }`,
                        style: {
                          backgroundColor: e.color,
                          animation: s
                            ? `energy-pulse-${e.logoPlacement}-fast 1.5s infinite linear`
                            : `energy-pulse-${e.logoPlacement} 3s infinite linear`,
                          transitionDuration: "300ms",
                        },
                        children: [
                          (0, t.jsx)("div", {
                            className:
                              "pointer-events-none absolute -inset-3 rounded-full",
                            style: {
                              background: `radial-gradient(circle, ${e.color}75 0%, ${e.color}28 42%, transparent 72%)`,
                            },
                          }),
                          (0, t.jsx)("div", {
                            className:
                              "pointer-events-none absolute -inset-1 rounded-full",
                            style: {
                              background: `radial-gradient(circle, #ffffff 0%, ${e.color} 24%, transparent 70%)`,
                              opacity: s ? 0.95 : 0.72,
                            },
                          }),
                        ],
                      }),
                    ],
                  }),
                !n &&
                  (0, t.jsx)("div", {
                    className: `skill-label absolute -translate-y-1/2 transition-[opacity,transform] duration-300 ${
                      s ? "z-30" : "z-20"
                    }`,
                    style: {
                      ...c.skillLabelStyles,
                      opacity: 1,
                      visibility: "visible",
                      pointerEvents: "none",
                    },
                    role: "tooltip",
                    "aria-live": "polite",
                    children: (0, t.jsx)("div", {
                      className: "pointer-events-auto",
                      children: (0, t.jsxs)(p.CyberCard, {
                        shape: (a % 5) + 1,
                        lean: !0,
                        glowColor: e.color,
                        containerClassName: "large-display-skill-card",
                        className:
                          "pl-[7.5%] pr-2.5 pt-6 pb-3 3xl:pr-3.5 3xl:pt-7 3xl:pb-3.5 4xl:pr-4 4xl:pb-4 font-mono transition-[opacity,transform,border-color,background-color,color] duration-300 cursor-pointer",
                        backgroundColor: "rgba(0,0,0,0.95)",
                        isStatic: !0,
                        children: [
                          (0, t.jsxs)("div", {
                            className:
                              "flex justify-between items-center w-full",
                            children: [
                              (0, t.jsxs)("div", {
                                className:
                                  "flex flex-col items-start text-left flex-grow",
                                children: [
                                  (0, t.jsx)("div", {
                                    className:
                                      "text-[13px] 3xl:text-[15px] 4xl:text-base font-black tracking-normal text-left leading-tight",
                                    style: {
                                      color: e.color,
                                      textShadow: `0 0 15px ${e.color}60`,
                                    },
                                    children: e.name,
                                  }),
                                  (0, t.jsx)("div", {
                                    className:
                                      "text-[8px] 3xl:text-[9px] 4xl:text-[10px] opacity-72 font-semibold mt-1.5 text-left leading-none whitespace-nowrap",
                                    style: { color: e.color },
                                    children: e.summary,
                                  }),
                                  (0, t.jsx)("div", {
                                    className:
                                      "text-[9px] 3xl:text-[10px] 4xl:text-[11px] uppercase tracking-wider opacity-60 font-black mt-2 text-left leading-none",
                                    style: { color: e.color },
                                    children: w(e.mastery),
                                  }),
                                  (0, t.jsx)(S, {
                                    level: k(e.mastery),
                                    color: e.color,
                                  }),
                                ],
                              }),
                              (0, t.jsx)("div", {
                                className:
                                  "flex flex-col items-center flex-shrink-0 -mr-0.5",
                                children: (0, t.jsx)(j, {
                                  level: k(e.mastery),
                                  color: e.color,
                                  size: o >= 1900 ? 52 : 46,
                                  isMaxed: 12 === k(e.mastery),
                                }),
                              }),
                            ],
                          }),
                          (0, t.jsx)("div", {
                            className: `overflow-hidden transition-[max-height,opacity,margin,padding] duration-300 ${
                              s
                                ? "max-h-32 opacity-100 mt-2 border-t border-light-200/5 pt-2"
                                : "max-h-0 opacity-0 mt-0 pt-0"
                            }`,
                            children: (0, t.jsx)("div", {
                              className: `origin-top transform-gpu transition-transform duration-300 ${
                                s ? "scale-y-100" : "scale-y-0"
                              }`,
                              children: (0, t.jsx)("div", {
                                className: "flex flex-wrap gap-1.5",
                                children: e.tags?.map((a) =>
                                  (0, t.jsx)(
                                    "span",
                                    {
                                      className:
                                        "text-[8px] 3xl:text-[9px] 4xl:text-[10px] px-2 py-1 3xl:px-2.5 rounded-sm border font-bold tracking-[0.08em]",
                                      style: {
                                        color: e.color,
                                        borderColor: `${e.color}45`,
                                        backgroundColor: `${e.color}12`,
                                      },
                                      children: a,
                                    },
                                    a
                                  )
                                ),
                              }),
                            }),
                          }),
                          (0, t.jsx)("div", {
                            className: `text-[8px] 3xl:text-[9px] 4xl:text-[10px] tracking-[0.18em] opacity-35 transition-[opacity,color,transform] duration-300 text-left ${
                              s ? "mt-2" : "mt-1"
                            }`,
                            children: (0, t.jsx)("span", { children: e.label }),
                          }),
                        ],
                      }),
                    }),
                  }),
              ],
            },
            `${e.name}-${a}`
          );
        }
      );
    (L.displayName = "SkillButton"),
      e.s(
        [
          "default",
          0,
          function () {
            let e = (0, h.useSkills)(),
              a = e.length > 0 ? e : R,
              s = (0, d.useRef)(null),
              r = (0, d.useRef)(null),
              [l, i] = (0, d.useState)(null),
              [n, o] = (0, d.useState)($),
              [p, x] = (0, d.useState)(window.innerWidth),
              [y, g] = (0, d.useState)(null),
              [b, v] = (0, d.useState)(!1);
            (0, d.useEffect)(() => {
              let e = () => {
                x(window.innerWidth), o($());
              };
              e(), window.addEventListener("resize", e, { passive: !0 });
              let t = (0, f.subscribeToCapabilityChanges)(e);
              return () => {
                window.removeEventListener("resize", e), t();
              };
            }, []);
            let k = (0, d.useCallback)(
                (e) => {
                  n || i(e);
                },
                [n]
              ),
              w = (0, d.useCallback)(() => {
                n || i(null);
              }, [n]),
              j = (0, d.useCallback)((e) => {
                g(e), v(!0);
              }, []),
              S = (0, d.useMemo)(
                () =>
                  null === l
                    ? null
                    : Array.from({ length: 12 }).map((e, s) => {
                        let r = 30 * s,
                          i = 0.2 * s,
                          n = `sun-ray-smooth-move-${s % 3}`;
                        return (0, t.jsx)(
                          "g",
                          {
                            style: {
                              transform: `rotate(${r}deg)`,
                              transformOrigin: "50% 50%",
                            },
                            children: (0, t.jsx)("line", {
                              x1: "50%",
                              y1: "50%",
                              x2: "50%",
                              y2: "0%",
                              stroke: a[l].color,
                              strokeWidth: "1",
                              strokeOpacity: "0.3",
                              style: {
                                transformOrigin: "50% 50%",
                                animation: `sun-ray-random-visibility 6s infinite ease-in-out ${i}s, ${n} 8s infinite ease-in-out ${
                                  i + 0.3
                                }s`,
                              },
                            }),
                          },
                          `ray-group-${r}-${a[l].name}`
                        );
                      }),
                [a, l]
              ),
              N = null !== y ? a[y] : null;
            return (0, t.jsxs)("section", {
              ref: s,
              id: "skills",
              className: "relative py-24",
              children: [
                (0, t.jsx)("div", {
                  className:
                    "absolute inset-0 bg-gradient-to-b from-black/70 via-black/30 to-black/70 z-1 pointer-events-none",
                }),
                (0, t.jsxs)("div", {
                  className: "container mx-auto px-page relative z-10",
                  children: [
                    (0, t.jsx)(m.SectionTitle, {
                      title: "SKILLS",
                      subtitle:
                        "Seven centers, root to crown. Nobody ever finishes a language, these are the seven I keep sharpening.",
                      marqueeText: "TECHNICAL EXPERTISE",
                      marqueeOffset: -30,
                      align: "start",
                    }),
                    n
                      ? (0, t.jsx)(P, { onSkillClick: j, skills: a })
                      : (0, t.jsxs)("div", {
                          ref: r,
                          className:
                            "relative w-[min(100%,calc(100svh*0.75),900px)] mx-auto large-display-skills",
                          id: "skeleton-container",
                          style: { aspectRatio: "3/4" },
                          children: [
                            null !== l &&
                              (0, t.jsxs)(t.Fragment, {
                                children: [
                                  (0, t.jsx)("div", {
                                    className:
                                      "absolute inset-0 pointer-events-none",
                                    style: {
                                      zIndex: -4,
                                      mixBlendMode: "screen",
                                    },
                                    children: (0, t.jsx)("svg", {
                                      className:
                                        "absolute inset-0 w-full h-full",
                                      style: { overflow: "visible" },
                                      "aria-hidden": "true",
                                      children: S,
                                    }),
                                  }),
                                  (0, t.jsx)("div", {
                                    className:
                                      "absolute inset-0 pointer-events-none z-10 transition-[opacity,transform] duration-300",
                                    style: {
                                      zIndex: -1,
                                      opacity: +(null !== l),
                                      transform: "translateZ(0)",
                                      willChange: "opacity, transform",
                                    },
                                    children: (0, t.jsx)(c.default, {
                                      src: "/assets/images/skills-chakra-5.webp",
                                      alt: "Glowing skeleton background",
                                      fill: !0,
                                      sizes:
                                        "(max-width: 768px) 100vw, (min-width: 1900px) 900px, 680px",
                                      className: "object-contain",
                                      priority: !0,
                                      style: {
                                        filter: `blur(7px) brightness(1.16) drop-shadow(0 0 9px ${a[l].color})`,
                                        mixBlendMode: "screen",
                                        opacity: 0.62,
                                        transform: "translateZ(0)",
                                      },
                                    }),
                                  }),
                                ],
                              }),
                            (0, t.jsx)("div", {
                              className: "absolute inset-0 z-10",
                              children: (0, t.jsx)(c.default, {
                                src: "/assets/images/skills-chakra-5.webp",
                                alt: "Cyberpunk skeleton with chakra points",
                                fill: !0,
                                sizes:
                                  "(max-width: 768px) 100vw, (min-width: 1900px) 900px, 680px",
                                className: "object-contain",
                                priority: !0,
                              }),
                            }),
                            (0, t.jsx)(u.RageEffectShader, {
                              hoveredSkill: l,
                              intensity: null !== l ? 5 : 0.9,
                              skills: a,
                              containerRef: r,
                            }),
                            (0, t.jsx)("div", {
                              className:
                                "absolute inset-0 z-20 pointer-events-auto",
                              children: a.map((e, a) =>
                                (0, t.jsx)(
                                  L,
                                  {
                                    skill: e,
                                    index: a,
                                    isHovered: l === a,
                                    onHover: k,
                                    onLeave: w,
                                    onClick: j,
                                    isMobile: n,
                                    windowWidth: p,
                                  },
                                  e.name
                                )
                              ),
                            }),
                          ],
                        }),
                  ],
                }),
                (0, t.jsx)(O, {
                  activeSkill: N,
                  isOpen: b,
                  onClose: () => v(!1),
                  selectedSkill: y,
                }),
              ],
            });
          },
        ],
        339153
      );
  },
]);
