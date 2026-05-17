import { defineConfig } from "vitepress";

export default defineConfig({
    title: "Periodic Table",
    appearance: "force-dark",
    description:
        "Periodic Table & Quantum Mechanics — An interactive exploration of atomic structure",
    lang: "en-US",
    cleanUrls: true,
    base: "/periodic-table/",

    themeConfig: {
        nav: [
            { text: "Home", link: "/" },
            { text: "Tables", link: "/sheets/table-1" },
            { text: "Chapters", link: "/chapters/0-introduction" },
            { text: "Annex", link: "/annex/math" },
        ],
        sidebar: [
            {
                text: "Periodic Tables",
                items: [
                    { text: "18-column Table", link: "/sheets/table-1" },
                    { text: "32-column Table", link: "/sheets/table-2" },
                ],
            },
            {
                text: "Quantum Mechanics",
                items: [
                    { text: "Introduction", link: "/chapters/0-introduction" },
                    {
                        text: "1. The Schrödinger Equation",
                        link: "/chapters/1-heart",
                    },
                    {
                        text: "2. Particle in a 1D Box",
                        link: "/chapters/2-1d-box",
                    },
                    {
                        text: "3. The 3D Hydrogen Atom",
                        link: "/chapters/3-hydrogen",
                    },
                    {
                        text: "4. Angular Solutions",
                        link: "/chapters/4-angular",
                    },
                    { text: "5. Radial Solutions", link: "/chapters/5-radial" },
                    {
                        text: "6. Spin & Periodic Table",
                        link: "/chapters/6-spin",
                    },
                    { text: "Quiz", link: "/chapters/7-quiz" },
                ],
            },
            {
                text: "Annex",
                items: [
                    { text: "Math Reference", link: "/annex/math" },
                    { text: "All Elements", link: "/annex/all-elements" },
                    { text: "Links", link: "/annex/links" },
                ],
            },
        ],
        socialLinks: [
            {
                icon: "github",
                link: "https://github.com/oscar6echo/periodic-table",
            },
        ],
        outline: "deep",
    },

    markdown: {
        math: true,
    },
});
