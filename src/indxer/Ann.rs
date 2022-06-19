use faiss::{index::IndexImpl, read_index};
use faiss::{index_factory, Index, MetricType};
use log::{info, trace, warn};

pub struct FaissIndex {
    all_index: IndexImpl,
}

impl FaissIndex {
    pub fn new(path_of_index: String) -> Self {
        let read_mod_index = match read_index(path_of_index) {
            Ok(t) => t,
            Err(e) => {
                warn!("{}", e);
                panic!("{}", e);
            }
        };
        FaissIndex {
            all_index: read_mod_index,
        }
    }

    pub fn create_new_index(){
        
    }
}
