import { app } from "/scripts/app.js";

console.log("📂 Loaded Seed SS Manager extension");

app.registerExtension({
    name: "SeedSSManager",

    nodeCreated(node) {
        if (node.comfyClass === "SeedSSManager") {
            console.log("✅ Seed SS Manager JS loaded for node:", node);
        }
    }
});