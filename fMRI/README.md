# ABCD fMRI

A key component of the ABCD Study involves several fMRI tasks administered to youth participants at baseline and every 2 years thereafter. 

Those tasks include:

* Monetary Incentive Delay (MID) Task (Knutson et al., [2000](https://doi.org/10.1006/nimg.2000.0593))
* Stop Signal Task (SST) (Logan [1984](https://psycnet.apa.org/record/1994-97487-005))
* Emotional N-Back Task (nBack) (Cohen et al., 2016b)


## fMRI processing (taken from Hagler et al. [2019](https://doi.org/10.1016/j.neuroimage.2019.116091))

### Preprocessing

The ABCD coordinators apply a standard set of preprocessing steps to all but the raw fMRI data. See Hagler et al. [2019](https://doi.org/10.1016/j.neuroimage.2019.116091) for details. Broadly:

* Head motion is corrected using AFNI's `3dvolreg`
    * This produces head motion time course estimates
* B<sub>0</sub> distortion, distortions due to gradient nonlinearities, and between-scan motion is corrected
* Automated registration to T1w images


Resulting images are in "native-space" with 2.4mm isotropic resolution

### Pre-analysis processing

* Initial frames are removed
* Voxel time series are normalized by dividing by the mean across time of each voxel
* Each subject's pre-processed time course is sampled onto the cortical surface using FreeSurfer's `mri_vol2surf`

### Generating nuissance regressors
1. Motion estimates and their derivatives (tx, ty, tz, rx, ry, rz, dtx, dty, dtz, drx, dry, drz)
    * These are filtered using infinite impulse response (IIR) to attenuate signals associated with respiration (0.31-0.43 Hz). See Fair et al. [2018](https://doi.org/10.1016/j.neuroimage.2019.116400)
2. Censoring vector for images with framewise displacement (FD) > 0.9mm (i.e., 1 if censored, 0 otherwise)

### General linear model (GLM)
* Task-related strength is estimated using a GLM at the individual subject level (implemented using AFNI's `3dDeconvolve`)
* Hemodynamic response functions (HRFs) are modelled using a gamma variate basic function and its temporal derrivative.
    * This is implemented in `abcd_hrf.py`
