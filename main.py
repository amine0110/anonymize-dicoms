import pydicom as pm
from glob import glob
from tqdm import tqdm

path_to_dicoms = 'path/to/all/dicoms/*'
out_path_dicom = 'anony_slice.dcm'


def anonymize_dicom(in_path, out_path, patient_name='Anonymous'):
    dicom_file = pm.dcmread(in_path)
    dicom_file.PatientName = patient_name
    dicom_file.save_as(out_path)


if __name__ == '__main__':
    for slice_ in tqdm(glob(path_to_dicoms)):
        anonymize_dicom(slice_, slice_)