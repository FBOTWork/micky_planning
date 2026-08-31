<div align="center">

<img width="2038" height="307" alt="Image" src="https://github.com/user-attachments/assets/4c0989b7-7735-4f69-be62-e7051cb16356" />

</div>

## Overview
This is a group of ROS2 packages responsible for task planning features of [FBOT@Work](https://fbotwork.vercel.app/) industrial robot (MICKY) in RoboCup@Work league.

---

## Architecture

The system consists of two main packages:

```
micky_planning/
├── 📁 micky_planning/      # Core planning algorithms
```

---

## Prerequisites

- ROS2 Humble
- Python 3.10+
- Ubuntu 22.04
- ROS dependencies are listed in `package.xml` and Python dependencies are in `requirements.txt`.

---

## Development

### Creating a New Feature

1. Switch to the `release` branch (`git checkout release`)
2. Update local branch with `git fetch` then `git pull`
3. Create a feature branch (`git checkout -b feature/feature-name`)
4. Create feature directory in `micky_planning/feature_name/`
5. Implement the feature
6. Update `__init__.py` imports
7. Add launch file in `launch/`
8. Add feature node to `setup.py`
9. Test and verify that the feature is fully functional
10. Commit changes (`git commit -m 'Add feature-name'`)
11. Push the branch (`git push`)
12. Open a Pull Request from `feature/feature-name` to `release` and add a reviewer
13. After review and validation, merge the Pull Request into `release`
14. Once `release` is tested and stable, merge it into `master`

### Fixing a Feature

1. Switch to the `release` branch (`git checkout release`)
2. Update local branch with `git fetch` then `git pull`
3. Create a fix branch (`git checkout -b fix/broken-feature`)
4. Fix a feature
5. Commit changes (`git commit -m 'Fix amazing feature'`)
6. Push to the branch (`git push`)
7. Open a Pull Request from `fix/feature-name` to `release` and add a reviewer
8. After review and validation, merge the Pull Request into `release`
9. Once `release` is tested and stable, merge it into `master`

---
