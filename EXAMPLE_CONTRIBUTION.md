# Example Contribution Workflow for git-helper

This document shows how contributors can help with git-helper and earn points in drips.network waves.

## Finding Work

Look for issues labeled with:
- `difficulty: trivial` (1 point)
- `difficulty: medium` (3 points)  
- `difficulty: high` (5 points)

## Making Your First Contribution (Trivial - 1 Point)

Let's say you see this issue:
```
[Trivial] Add missing help text for branch cleanup command
```

Here's how you'd contribute:

1. **Fork the repository**
2. **Create a branch**: `git checkout -b fix/branch-cleanup-help`
3. **Make your change**: Edit `src/git_helper/cli.py` to add better help text
4. **Test your change**: 
   ```bash
   python3 -m src.git_helper.cli branch --help
   ```
5. **Commit**: `git commit -m "add: improve help text for branch cleanup"`
6. **Push**: `git push origin fix/branch-cleanup-help`
7. **Open a Pull Request**

## Medium Contribution Example (3 Points)

```
[Medium] Add "branch cleanup" command to remove old branches
```

Steps:
1. Fork and branch as before
2. Implement the branch cleanup functionality in the cli.py
3. Add tests for the new functionality
4. Update documentation if needed
5. Submit PR

## High Contribution Example (5 Points)

```
[High] Implement interactive PR creation with templates
```

This would involve:
- Designing an interactive workflow
- Integrating with GitHub API (if desired)
- Adding configuration options
- Comprehensive testing
- Documentation updates

## Getting Points

Once your PR is merged:
1. The maintainer will verify your contribution
2. You'll receive the appropriate points based on issue difficulty
3. Points are tracked in the drips.network wave system
4. You can redeem points for rewards during the wave period

## Tips for Success

- Start with trivial issues to get familiar with the codebase
- Read the CONTRIBUTING.md guidelines before starting
- Keep PRs focused on a single issue
- Write clear commit messages
- Be responsive to feedback in code reviews
- Have fun contributing!
