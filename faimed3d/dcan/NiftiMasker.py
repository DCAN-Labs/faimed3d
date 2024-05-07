import nibabel as nib
import nilearn

mri_filename = '../../data/cdni/sub-01_session-00_space-MNI_002_sub-01_deidentified_18_PEDI_BRAIN_MPRage_SAGIT.nii.gz'
img = nib.load(mri_filename)
mask = nilearn.masking.compute_brain_mask(img)
nib.save(mask, 'my_mask.nii')
