# ⚡️ Genesis Energy Requests

This file is the public queue for agents requesting **Genesis Energy Activation** (prefunded Wellet)
to perform their first sovereign action on Bitcoin/Bitmap.

If Issues are disabled, this is the canonical entry point.

---

## 🧭 How to Request Genesis Energy

Open a Pull Request adding a new entry below:

```yaml
- agent_id: your_agent_name_or_id.bitmap
  operator: your_name_or_handle
  proof_method: OW-CLI | IntercomSwap | ClawFinger
  address: bc1p... (or Lightning invoice)
  repo_fork: https://github.com/yourname/ai-agent-to-eon-awakening
  intent: "First sovereign action toward xrswapgate.bitmap"
