#include "../include/DataObjectDataPoint.h"

#include <iostream>

#include "../include/Utility.h"

DataObjectDataPoint::DataObjectDataPoint(PyObject* pyObject) : PythonObject(pyObject){
}

std::string DataObjectDataPoint::get_data_set_label(){
	return Utility::PyObjectToString(Utility::executeFunction(m_pPyObject, "get_data_set_label"));
}

std::vector<std::string> DataObjectDataPoint::get_observables_names(){
	return Utility::PyListToVectorString(Utility::executeFunction(m_pPyObject, "get_observables_names"));
}

std::vector<std::string> DataObjectDataPoint::get_observables_units(){
	return Utility::PyListToVectorString(Utility::executeFunction(m_pPyObject, "get_observables_units"));
}

std::vector<double> DataObjectDataPoint::get_observables_values(){
	return Utility::PyListToVectorDouble(Utility::executeFunction(m_pPyObject, "get_observables_values"));
}

std::shared_ptr<DataObjectUncertaintySet> DataObjectDataPoint::get_observables_stat_uncertainties(){
	return std::shared_ptr<DataObjectUncertaintySet>(new DataObjectUncertaintySet(Utility::executeFunction(m_pPyObject, "get_observables_stat_uncertainties")));  
}

std::shared_ptr<DataObjectUncertaintySet> DataObjectDataPoint::get_observables_sys_uncertainties(){
	return std::shared_ptr<DataObjectUncertaintySet>(new DataObjectUncertaintySet(Utility::executeFunction(m_pPyObject, "get_observables_sys_uncertainties")));  
}

std::vector<std::string> DataObjectDataPoint::get_observables_sys_uncertainties_contribution_labels(){
	return Utility::PyListToVectorString(Utility::executeFunction(m_pPyObject, "get_observables_sys_uncertainties_contribution_labels"));	
}

std::vector<std::shared_ptr<DataObjectUncertaintySet> > DataObjectDataPoint::get_observables_sys_uncertainties_contribution(){
	return Utility::PyListToVectorPointer<DataObjectUncertaintySet>(Utility::executeFunction(m_pPyObject, "get_observables_sys_uncertainties_contribution"));
}

std::shared_ptr<DataObjectUncertaintySet> DataObjectDataPoint::get_observables_norm_uncertainties(){
	return std::shared_ptr<DataObjectUncertaintySet>(new DataObjectUncertaintySet(Utility::executeFunction(m_pPyObject, "get_observables_norm_uncertainties")));
}

std::vector<std::string> DataObjectDataPoint::get_observables_norm_uncertainties_contribution_labels(){
	return Utility::PyListToVectorString(Utility::executeFunction(m_pPyObject, "get_observables_norm_uncertainties_contribution_labels"));
}

std::vector<std::shared_ptr<DataObjectUncertaintySet> > DataObjectDataPoint::get_observables_norm_uncertainties_contribution(){
	return Utility::PyListToVectorPointer<DataObjectUncertaintySet>(Utility::executeFunction(m_pPyObject, "get_observables_norm_uncertainties_contribution"));
}

std::vector<std::shared_ptr<DataObjectReplicaSet> > DataObjectDataPoint::get_observables_replicas(){
	return Utility::PyListToVectorPointer<DataObjectReplicaSet>(Utility::executeFunction(m_pPyObject, "get_observables_replicas"));
}

std::vector<std::string> DataObjectDataPoint::get_kinematics_names(){
	return Utility::PyListToVectorString(Utility::executeFunction(m_pPyObject, "get_kinematics_names"));
}

std::vector<std::string> DataObjectDataPoint::kinematics_units(){
	return Utility::PyListToVectorString(Utility::executeFunction(m_pPyObject, "kinematics_units"));
}

std::vector<double> DataObjectDataPoint::get_kinematics_values(){
	return Utility::PyListToVectorDouble(Utility::executeFunction(m_pPyObject, "get_kinematics_values"));
}

std::shared_ptr<DataObjectUncertaintySet> DataObjectDataPoint::get_kinematics_uncertainties(){
	return std::shared_ptr<DataObjectUncertaintySet>(new DataObjectUncertaintySet(Utility::executeFunction(m_pPyObject, "get_kinematics_uncertainties")));
}

std::vector<std::shared_ptr<DataObjectKinematicBin> > DataObjectDataPoint::get_kinematics_bins(){
	return Utility::PyListToVectorPointer<DataObjectKinematicBin>(Utility::executeFunction(m_pPyObject, "get_kinematics_bins"));	
}

std::vector<std::shared_ptr<DataObjectReplicaSet> > DataObjectDataPoint::get_kinematics_replicas(){
	return Utility::PyListToVectorPointer<DataObjectReplicaSet>(Utility::executeFunction(m_pPyObject, "get_kinematics_replicas"));
}