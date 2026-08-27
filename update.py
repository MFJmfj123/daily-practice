import re

# Update index.html
with open(r"M:\cursor_project\daka_project\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove goals nav item
html = html.replace('<button class="nav-item" data-view="goals"><span class="nav-icon">\u25c8</span><span>长远目标</span></button>\n', '')

# Add habit modal before </main>
habit_modal = '''
        <!-- 新建习惯模态框 -->
        <div class="modal-backdrop hidden" id="habitModal" role="dialog" aria-modal="true" aria-labelledby="habitModalTitle">
          <section class="modal">
            <button class="modal-close icon-button" id="closeHabitModal" title="关闭">\u00d7</button>
            <div class="eyebrow">NEW HABIT / 新习惯</div>
            <h2 id="habitModalTitle">新建习惯</h2>
            <p class="modal-intro">为每天的小行动赋予意义，让它成为你的一部分。</p>
            <form id="habitForm">
              <label>习惯名称 <input id="habitName" placeholder="例如：阅读 20 分钟" required /></label>
              <label>描述 <input id="habitDesc" placeholder="一句话描述这个习惯的意义" /></label>
              <label>颜色主题
                <div class="color-picker" id="colorPicker">
                  <span class="color-option active" data-color="rust">\u94c1\u7f38\u7ea2</span>
                  <span class="color-option" data-color="forest">\u68ee\u6797\u7eff</span>
                  <span class="color-option" data-color="gold">\u79cb\u91d1\u8272</span>
                  <span class="color-option" data-color="sky">\u5929\u7a7a\u84dd</span>
                </div>
              </label>
              <div class="modal-actions">
                <button type="button" class="secondary-button" id="cancelHabitModal">\u53d6\u6d88</button>
                <button type="submit" class="primary-button" id="habitSubmit">\u4fdd\u5b58\u4e60\u60ef</button>
              </div>
            </form>
            <div class="settings-feedback" id="habitFeedback"></div>
          </section>
        </div>
'''

# Add modal after habits section
html = html.replace('</section>\n\n        <aside class="right-rail">', habit_modal + '\n      </main>\n\n      <aside class="right-rail">')

# Change today page button
html = html.replace('<button class="add-habit-button" data-view="habits">', '<button class="add-habit-button" id="openHabitModal">')

with open(r"M:\cursor_project\daka_project\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated")

# Update app.js
with open(r"M:\cursor_project\daka_project\app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Add functions after loadData
new_funcs = '''
function escapeHtml(text) { const div = document.createElement("div"); div.textContent = text; return div.innerHTML; }
function openHabitModal() {
  document.getElementById("habitName").value = "";
  document.getElementById("habitDesc").value = "";
  selectedColor = "rust";
  document.querySelectorAll(".color-option").forEach(el => el.classList.remove("active"));
  document.querySelector('.color-option[data-color="rust"]').classList.add("active");
  document.getElementById("habitModal").classList.remove("hidden");
}
function closeHabitModal() { document.getElementById("habitModal").classList.add("hidden"); }
'''
js = js.replace('let data = loadData();', 'let data = loadData();\nlet selectedColor = "rust";' + new_funcs)

# Replace old handler
old_handler = '''document.getElementById("newHabitButton").addEventListener("click", () => { const name = prompt("新习惯名称"); if (!name?.trim()) return; data.habits.push({ id: `${Date.now()}`, name: name.trim(), description: "一个值得持续的小行动。", color: "rust" }); persist(); toast("新习惯已添加"); });'''
new_handler = '''document.getElementById("newHabitButton").addEventListener("click", openHabitModal);
document.getElementById("openHabitModal").addEventListener("click", openHabitModal);
document.getElementById("closeHabitModal").addEventListener("click", closeHabitModal);
document.getElementById("cancelHabitModal").addEventListener("click", closeHabitModal);
document.querySelectorAll(".color-option").forEach(el => { el.addEventListener("click", () => { selectedColor = el.dataset.color; document.querySelectorAll(".color-option").forEach(o => o.classList.remove("active")); el.classList.add("active"); }); });
document.getElementById("habitForm").addEventListener("submit", event => { event.preventDefault(); const name = document.getElementById("habitName").value.trim(); if (!name) return; data.habits.push({ id: `${Date.now()}`, name, description: document.getElementById("habitDesc").value.trim() || "一个值得持续的小行动。", color: selectedColor }); persist(); closeHabitModal(); toast("新习惯已添加"); });'''
js = js.replace(old_handler, new_handler)

# Also update renderToday empty state text
js = js.replace('还没有习惯，从右上角新建一个吧。', '还没有习惯，点击添加一个吧。')

with open(r"M:\cursor_project\daka_project\app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("app.js updated")
