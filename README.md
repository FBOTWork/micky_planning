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

## Pre Requisites

- ROS2 Humble
- Python 3.10+
- Ubuntu 22.04
- ROS dependencies are listed in `package.xml` and Python dependencies are in `requirements.txt`.

---

## Development

### Creating a New Feature

1. Switch to the `release` branch (`git checkout release`)
2. Create a feature branch (`git checkout -b feature/feature-name`)
3. Create feature directory in `micky_planning/feature_name/`
4. Implement the feature
5. Update `__init__.py` imports
6. Add launch file in `launch/`
7. Add feature node to `setup.py`
8. Test and verify that the feature is fully functional
9. Commit changes (`git commit -m 'Add feature-name'`)
10. Push the branch (`git push`)
11. Open a Pull Request from `feature/feature-name` to `release` and add a reviewer
12. After review and validation, merge the Pull Request into `release`
13. Once `release` is tested and stable, merge it into `master`

### Fixing a Feature

1. Switch to the `release` branch (`git checkout release`)
2. Create a fix branch (`git checkout -b fix/broken-feature`)
3. Fix a feature
4. Commit changes (`git commit -m 'Fix amazing feature'`)
5. Push to the branch (`git push`)
6. Open a Pull Request from `fix/feature-name` to `release` and add a reviewer
7. After review and validation, merge the Pull Request into `release`
8. Once `release` is tested and stable, merge it into `master`

---