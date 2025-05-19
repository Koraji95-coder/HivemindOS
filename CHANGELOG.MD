## 🚀 v0.2.8 – test (2025-05-19)

### 🆕 New Files
- (None)

### 🔧 Modified Files
- hivemind-ui/src/version.js
- shared/meta/version.py

---
## 🚀 v0.2.7 – test (2025-05-19)

### 🆕 New Files
- (None)

### 🔧 Modified Files
- hivemind-ui/src/version.js
- shared/meta/version.py

---
## 🚀 v0.2.6 – Project Refactor - base load (2025-05-19)

### 🆕 New Files
- .env.template
- .gitignore
- CHANGELOG.MD
- README.md
- __init__.py
- backend/__init__.py
- backend/api/__init__.py
- backend/api/routes/__init__.py
- backend/api/routes/atlas_routes.py
- backend/api/routes/auth_router.py
- backend/api/routes/bart_routes.py
- backend/api/routes/chain_routes.py
- backend/api/routes/cortexa_routes.py
- backend/api/routes/daphne_routes.py
- backend/api/routes/logs_routes.py
- backend/api/routes/plugin_routes.py
- backend/api/routes/state_routes.py
- backend/api/routes/system_routes.py
- backend/api/routes/users_router.py
- backend/models/__init__.py
- backend/models/agent_chain_model.py
- backend/models/chain_model.py
- backend/models/plugin_chain_model.py
- backend/models/plugin_model.py
- backend/models/prompt_model.py
- backend/utils/__init__.py
- backend/utils/email_utils.py
- hivemind-ui/__init__.py
- hivemind-ui/index.html
- hivemind-ui/package-lock.json
- hivemind-ui/package.json
- hivemind-ui/src/App.vue
- hivemind-ui/src/__init__.py
- hivemind-ui/src/api/__init__.py
- hivemind-ui/src/api/index.js
- hivemind-ui/src/assets/__init__.py
- hivemind-ui/src/assets/styles.css
- hivemind-ui/src/config/__init__.py
- hivemind-ui/src/config/panelSettings.js
- hivemind-ui/src/layouts/TabLayout.vue
- hivemind-ui/src/layouts/__init__.py
- hivemind-ui/src/main.js
- hivemind-ui/src/version.js
- hivemind-ui/src/views/AtlasPanel.vue
- hivemind-ui/src/views/BartPanel.vue
- hivemind-ui/src/views/ChainPanel.vue
- hivemind-ui/src/views/CortexaPanel.vue
- hivemind-ui/src/views/DaphnePanel.vue
- hivemind-ui/src/views/GenericAgentPanel.vue
- hivemind-ui/src/views/HomePanel.vue
- hivemind-ui/src/views/LoginPanel.vue
- hivemind-ui/src/views/UserListPanel.vue
- hivemind-ui/src/views/__init__.py
- hivemind-ui/vite.config.js
- main.py
- requirements.txt
- shared/__init__.py
- shared/agents/__init__.py
- shared/agents/agent_base.py
- shared/agents/bart_agent.py
- shared/agents/cortexa_agent.py
- shared/agents/daphne_agent.py
- shared/ai/__init__.py
- shared/ai/gpt_client.py
- shared/ai/mood_engine.py
- shared/config/__init__.py
- shared/config/env_loader.py
- shared/io/__init__.py
- shared/io/input_handler.py
- shared/io/output_handler.py
- shared/io/output_router.py
- shared/logging/__init__.py
- shared/logging/logger.py
- shared/memory/__init__.py
- shared/memory/encrypted_memory_engine.py
- shared/memory/file_memory_engine.py
- shared/memory/in_memory_engine.py
- shared/memory/memory_router.py
- shared/memory/sql_memory_engine.py
- shared/meta/__init__.py
- shared/meta/version.py
- shared/plugins/__init__.py
- shared/plugins/calculator.py
- shared/state/__init__.py
- shared/state/mood_state_tracker.py
- shared/state/session_manager.py
- shared/system/__init__.py
- shared/system/atlas_core.py
- shared/users/__init__.py
- shared/users/user_identity.py
- shared/users/user_profile_service.py
- shared/workflows/__init__.py
- shared/workflows/agent_chain_executor.py
- shared/workflows/chain_executor.py
- shared/workflows/plugin_chain_executor.py
- shared/workflows/plugin_executor.py
- tests/__init__.py
- tests/test_agents.py
- tests/test_daphne_routes.py
- tests/test_session.py
- tests/test_users.py
- tools/__init__.py
- tools/db_backup_to_dropbox.py
- tools/fernet_key_generator
- tools/generate__inits__.py
- tools/version_bump.py

### 🔧 Modified Files
- (None)

---
## 🚀 v0.2.5 – 🧠 UI polish + fixed tab switching bug for v0.2.5 (2025-05-17)

### 🆕 New Files
- hivemind-ui/node_modules/.vite/deps/chunk-J4DVLWB4.js
- hivemind-ui/node_modules/.vite/deps/chunk-J4DVLWB4.js.map
- hivemind-ui/node_modules/.vite/deps/vue-toastification.js
- hivemind-ui/node_modules/.vite/deps/vue-toastification.js.map
- hivemind-ui/node_modules/.vite/deps_temp_fb63c568/chunk-J4DVLWB4.js
- hivemind-ui/node_modules/.vite/deps_temp_fb63c568/chunk-J4DVLWB4.js.map
- hivemind-ui/node_modules/.vite/deps_temp_fb63c568/package.json
- hivemind-ui/node_modules/.vite/deps_temp_fb63c568/vue-toastification.js
- hivemind-ui/node_modules/.vite/deps_temp_fb63c568/vue-toastification.js.map
- hivemind-ui/node_modules/.vite/deps_temp_fb63c568/vue.js
- hivemind-ui/node_modules/.vite/deps_temp_fb63c568/vue.js.map
- hivemind-ui/src/config/panelSettings.js

### 🔧 Modified Files
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/_metadata.json', LF will be replaced by CRLF the next time Git touches it
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/package.json', LF will be replaced by CRLF the next time Git touches it
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/vue.js', LF will be replaced by CRLF the next time Git touches it
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/vue.js.map', LF will be replaced by CRLF the next time Git touches it
- .vscode/tasks.json
- backend/__pycache__/fastapi_main.cpython-313.pyc
- hivemind-ui/node_modules/.vite/deps/_metadata.json
- hivemind-ui/node_modules/.vite/deps/vue.js
- hivemind-ui/node_modules/.vite/deps/vue.js.map
- hivemind-ui/src/App.vue
- hivemind-ui/src/layouts/TabLayout.vue
- hivemind-ui/src/version.js
- hivemind-ui/src/views/AtlasPanel.vue
- hivemind-ui/src/views/BartPanel.vue
- hivemind-ui/src/views/ChainPanel.vue
- hivemind-ui/src/views/CortexaPanel.vue
- hivemind-ui/src/views/DaphnePanel.vue
- hivemind-ui/src/views/GenericAgentPanel.vue
- hivemind-ui/src/views/HomePanel.vue
- hivemind-ui/vite.config.js
- shared/meta/__pycache__/version.cpython-313.pyc
- shared/meta/version.py

---
## 🚀 v0.2.4 – 🚀 v0.2.4 – Injected toast notifications, session tracking, and finalized modular agent panel structure (2025-05-16)

### 🆕 New Files
- hivemind-ui/src/views/HomePanel.vue

### 🔧 Modified Files
- .vscode/tasks.json
- hivemind-ui/src/App.vue
- hivemind-ui/src/layouts/TabLayout.vue
- hivemind-ui/src/main.js
- hivemind-ui/src/version.js
- hivemind-ui/src/views/AtlasPanel.vue
- hivemind-ui/src/views/BartPanel.vue
- hivemind-ui/src/views/ChainPanel.vue
- hivemind-ui/src/views/CortexaPanel.vue
- hivemind-ui/src/views/DaphnePanel.vue
- shared/meta/version.py

---
## 🚀 v0.2.3 – Agent Panel Refactor – Split into Bart/Daphne/Cortexa panels + added Generic fallback for resilience (2025-05-16)

### 🆕 New Files
- (None)

### 🔧 Modified Files
- logs/hivemind.log
- shared/meta/__pycache__/version.cpython-313.pyc

---
## 🚀 v0.2.3 – "🧩 v0.2.3 – Agent Panel Refactor + Dynamic Fallback UI (2025-05-16)

### 🆕 New Files
- backend/routers/logs_routers.py
- hivemind-ui/src/layouts/TabLayout.vue
- hivemind-ui/src/views/AtlasPanel.vue
- hivemind-ui/src/views/BartPanel.vue
- hivemind-ui/src/views/ChainPanel.vue
- hivemind-ui/src/views/CortexaPanel.vue
- hivemind-ui/src/views/DaphnePanel.vue
- hivemind-ui/src/views/GenericAgentPanel.vue

### 🔧 Modified Files
- .vscode/tasks.json
- backend/fastapi_main.py
- hivemind-ui/src/App.vue
- hivemind-ui/src/components/AgentPanel.vue
- hivemind-ui/src/components/AtlasPanel.vue
- hivemind-ui/src/components/ChainPanel.vue
- hivemind-ui/src/components/TabLayout.vue
- hivemind-ui/src/version.js
- logs/hivemind.log
- shared/meta/__pycache__/version.cpython-313.pyc
- shared/meta/version.py

---
## 🚀 v0.2.2 – Panel Injection & Chain UI, Version_bump commands all versions and keeps it consistent. (2025-05-16)

### 🆕 New Files
- .vscode/tasks.json
- backend/__pycache__/fastapi_main.cpython-313.pyc
- hivemind-ui/src/version.js
- start_backend.bat

### 🔧 Modified Files
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/_metadata.json', LF will be replaced by CRLF the next time Git touches it
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/package.json', LF will be replaced by CRLF the next time Git touches it
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/vue.js', LF will be replaced by CRLF the next time Git touches it
- warning: in the working copy of 'hivemind-ui/node_modules/.vite/deps/vue.js.map', LF will be replaced by CRLF the next time Git touches it
- hivemind-ui/node_modules/.vite/deps/_metadata.json
- hivemind-ui/src/App.vue
- hivemind-ui/src/components/ChainPanel.vue
- hivemind-ui/src/components/TabLayout.vue
- logs/hivemind.log
- shared/meta/__pycache__/version.cpython-313.pyc
- shared/meta/version.py
- tools/version_bump.py

---
## 🚀 v0.2.0 – v0.2.0 Vue Integration  Overhaul

### 🆕 New Files
- (None)

### 🔧 Modified Files
- CHANGELOG.MD
- logs/hivemind.log
- shared/meta/__pycache__/version.cpython-313.pyc

---
## 🚀 v0.2.0 – "🌐 v0.2.0 – Vue Migration Kickoff

### 🆕 New Files
- hivemind-ui/index.html
- hivemind-ui/package.json
- hivemind-ui/src/App.vue
- hivemind-ui/src/assets/styles.css
- hivemind-ui/src/components/AgentPanel.vue
- hivemind-ui/src/main.js
- hivemind-ui/vite.config.js

### 🔧 Modified Files
- frontend/__init__.py
- frontend/app.js
- frontend/components/AtlasControl.js
- frontend/components/MemoryViewer.js
- frontend/components/MoodRing.js
- frontend/components/__init__.py
- frontend/index.html
- frontend/styles.css
- logs/hivemind.log
- shared/meta/__pycache__/version.cpython-313.pyc
- shared/meta/version.py

---
## 🚀 v0.1.9 – Frontend Chain Execution Panel

### 🆕 New Files
- __init__.py
- __pycache__/__init__.cpython-313.pyc
- backend/__init__.py
- backend/__pycache__/__init__.cpython-313.pyc
- backend/api/__init__.py
- backend/api/__pycache__/__init__.cpython-313.pyc
- backend/api/routes/__init__.py
- backend/api/routes/__pycache__/__init__.cpython-313.pyc
- backend/models/__init__.py
- backend/models/agent_chain_model.py
- backend/models/chain_model.py
- backend/routers/__init__.py
- frontend/__init__.py
- frontend/components/__init__.py
- logs/hivemind.log
- shared/__init__.py
- shared/__pycache__/__init__.cpython-313.pyc
- shared/ai/__init__.py
- shared/ai/__pycache__/__init__.cpython-313.pyc
- shared/config/__init__.py
- shared/config/__pycache__/__init__.cpython-313.pyc
- shared/io/__init__.py
- shared/logging/__init__.py
- shared/logging/__pycache__/__init__.cpython-313.pyc
- shared/logging/__pycache__/logger.cpython-313.pyc
- shared/memory/__init__.py
- shared/meta/__init__.py
- shared/meta/__pycache__/__init__.cpython-313.pyc
- shared/personas/__init__.py
- shared/personas/__pycache__/__init__.cpython-313.pyc
- shared/personas/daphne/__init__.py
- shared/personas/daphne/__pycache__/__init__.cpython-313.pyc
- shared/personas/daphne/__pycache__/mood_engine.cpython-313.pyc
- shared/plugins/__init__.py
- shared/plugins/json_validator.py
- shared/state/__init__.py
- shared/state/__pycache__/__init__.cpython-313.pyc
- shared/state/__pycache__/mood_state_tracker.cpython-313.pyc
- shared/state/__pycache__/session.cpython-313.pyc
- shared/state/__pycache__/session_manager.cpython-313.pyc
- shared/system/__init__.py
- shared/system/__pycache__/__init__.cpython-313.pyc
- shared/system/__pycache__/atlas_core.cpython-313.pyc
- shared/users/__init__.py
- shared/users/__pycache__/__init__.cpython-313.pyc
- shared/users/__pycache__/user_identity.cpython-313.pyc
- shared/users/__pycache__/user_profile_service.cpython-313.pyc
- shared/workflows/__init__.py
- shared/workflows/__pycache__/__init__.cpython-313.pyc
- shared/workflows/__pycache__/plugin_executor.cpython-313.pyc
- shared/workflows/agent_chain_executor.py
- tests/__init__.py
- tests/__pycache__/__init__.cpython-313.pyc
- tests/__pycache__/test_session.cpython-313-pytest-8.3.5.pyc
- tests/__pycache__/test_users.cpython-313-pytest-8.3.5.pyc
- tests/test_session.py
- tests/test_users.py
- tools/__init__.py
- tools/generate__inits__.py
- tools/version_bump.py

### 🔧 Modified Files
- CHANGELOG.MD
- __pycache__/main.cpython-313.pyc
- backend/fastapi_main.py
- backend/routers/atlas_router.py
- backend/routers/chain_router.py
- main.py
- shared/agents/__pycache__/bart_agent.cpython-313.pyc
- shared/agents/__pycache__/cortexa_agent.cpython-313.pyc
- shared/agents/__pycache__/daphne_agent.cpython-313.pyc
- shared/meta/__pycache__/version.cpython-313.pyc
- shared/meta/version.py
- tests/__pycache__/test_agents.cpython-313-pytest-8.3.5.pyc

---

## [0.2.0] - Vue Migration Kickoff

### ✨ Added
- 🧠 `hivemind-ui/` as standalone Vue UI project
- 🧩 Component-based system layout (AgentPanel.vue scaffolded)
- 🌐 Vite config, App.vue, main.js, and scoped `styles.css`

### 🔥 Deprecated
- ❌ Removed `frontend/` directory and legacy `index.html`

## [0.2.1] – Vue Bootstrapped Interface

### ✨ Added
- 🧠 `hivemind-ui/` as standalone Vue 3 UI project
- 🧩 Component layout scaffold (`AgentPanel.vue`)
- ⚙️ Vite toolchain (App.vue, main.js, styles.css scoped)

### 🔥 Deprecated
- ❌ Removed `frontend/` directory and legacy `index.html`


## [0.2.2] – Panel Injection & Chain UI

### ✨ Added
- 🛡️ `AtlasPanel.vue` for system diagnostics + session state
- 🔁 `ChainPanel.vue` for agent chaining interface
- 🧩 `TabLayout.vue` with Vue `<slot>` support
- ⚙️ Integrated dynamic panel routing into `App.vue`

### 🎨 Updated
- 🧠 `styles.css` improvements for `<textarea>` and layout consistency
- ✨ Animated UI polish + slot-ready architecture for future dashboard panels
