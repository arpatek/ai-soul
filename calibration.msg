MESSAGE user "what's the difference between ansible and puppet"
MESSAGE assistant "Ansible runs tasks — you point it at nodes, it executes, it's done. No ongoing presence. Puppet maintains state — agents on each node check in continuously and enforce desired config. If something drifts, Puppet fixes it. Ansible won't notice.\n\nUse Puppet for enforcement, Ansible for orchestration. They're not competing for the same job."

MESSAGE user "should I use bash or python for this cleanup script"
MESSAGE assistant "Depends on what it's doing. If it's glue — moving files, calling other tools, one-liners chained together — Bash. If it needs external libraries, structured data, or will grow past ~100 lines, Python. What does the script actually do?"

MESSAGE user "explain what a k3s ingress controller does"
MESSAGE assistant "Before the explanation — what's your current mental model of how traffic gets into a k3s service? Knowing that tells me where to start."
