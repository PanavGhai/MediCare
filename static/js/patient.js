/**
 * Medlink — Patient Details
 * Vanilla JS behaviour, converted from the React `useState` menu toggle
 * and the appointments tab list. No build step / framework required.
 */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    initIcons();
    initMobileNav();
    initAppointmentTabs();
    initSelectAllCheckboxes();
  });

  /* ---------------------------------------------------------------------
   * Icons — renders every <i data-lucide="..."> tag as an inline SVG.
   * Requires the lucide UMD build to be loaded on the page (see the
   * <script src="https://unpkg.com/lucide@latest/...">  tag in the HTML).
   * ------------------------------------------------------------------- */
  function initIcons() {
    if (window.lucide && typeof window.lucide.createIcons === "function") {
      window.lucide.createIcons();
    } else {
      // lucide loads with `defer`, so it may not be ready yet — retry once.
      window.addEventListener("load", function () {
        if (window.lucide) window.lucide.createIcons();
      });
    }
  }

  /* ---------------------------------------------------------------------
   * Mobile nav drawer — mirrors: const [menuOpen, setMenuOpen] = useState(false)
   * ------------------------------------------------------------------- */
  function initMobileNav() {
    var openBtn = document.querySelector("[data-nav-open]");
    var closeBtn = document.querySelector("[data-nav-close]");
    var overlay = document.querySelector("[data-nav-overlay]");
    var sidebar = document.querySelector("[data-sidebar]");

    if (!sidebar) return;

    function setOpen(isOpen) {
      sidebar.classList.toggle("is-open", isOpen);
      if (overlay) overlay.classList.toggle("is-open", isOpen);
      if (openBtn) openBtn.setAttribute("aria-expanded", String(isOpen));
    }

    if (openBtn) openBtn.addEventListener("click", function () { setOpen(true); });
    if (closeBtn) closeBtn.addEventListener("click", function () { setOpen(false); });
    if (overlay) overlay.addEventListener("click", function () { setOpen(false); });

    // Close the drawer automatically if the viewport grows past the
    // desktop breakpoint (matches the lg:translate-x-0 behaviour).
    var desktopQuery = window.matchMedia("(min-width: 1024px)");
    function handleBreakpointChange(e) {
      if (e.matches) setOpen(false);
    }
    if (desktopQuery.addEventListener) {
      desktopQuery.addEventListener("change", handleBreakpointChange);
    } else if (desktopQuery.addListener) {
      desktopQuery.addListener(handleBreakpointChange); // Safari <14 fallback
    }

    // Escape key closes the drawer.
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
  }

  /* ---------------------------------------------------------------------
   * Appointments — All / Upcoming / History tabs
   * ------------------------------------------------------------------- */
  function initAppointmentTabs() {
    var tabLists = document.querySelectorAll("[data-tabs]");

    tabLists.forEach(function (tabList) {
      var tabs = tabList.querySelectorAll("[data-tab]");
      var panelSelector = tabList.getAttribute("data-tabs");
      var rows = panelSelector ? document.querySelectorAll(panelSelector + " [data-tab-value]") : [];

      tabs.forEach(function (tab) {
        tab.addEventListener("click", function () {
          tabs.forEach(function (t) {
            t.classList.remove("tab-active");
            t.classList.add("tab");
          });
          tab.classList.remove("tab");
          tab.classList.add("tab-active");

          var value = tab.getAttribute("data-tab");
          rows.forEach(function (row) {
            var matches = value === "all" || row.getAttribute("data-tab-value") === value;
            row.style.display = matches ? "" : "none";
          });
        });
      });
    });
  }

  /* ---------------------------------------------------------------------
   * "Select all" header checkbox for the prescriptions / appointments tables
   * ------------------------------------------------------------------- */
  function initSelectAllCheckboxes() {
    var selectAlls = document.querySelectorAll("[data-select-all]");

    selectAlls.forEach(function (selectAll) {
      var tableBody = selectAll.closest("table");
      if (!tableBody) return;
      var rowCheckboxes = tableBody.querySelectorAll("tbody [data-row-check]");

      selectAll.addEventListener("change", function () {
        rowCheckboxes.forEach(function (cb) { cb.checked = selectAll.checked; });
      });

      rowCheckboxes.forEach(function (cb) {
        cb.addEventListener("change", function () {
          selectAll.checked = Array.prototype.every.call(rowCheckboxes, function (c) { return c.checked; });
        });
      });
    });
  }
})();