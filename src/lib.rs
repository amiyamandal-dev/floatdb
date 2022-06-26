use bytevec::ByteEncodable;
use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn generate_hash(a: Vec<f64>) -> PyResult<String> {
    let bytes = match a.encode::<u32>() {
        Ok(t) => t,
        Err(e) => panic!("{:?}", e),
    };
    let digest = md5::compute(bytes);
    Ok(format!("{:x}", digest))
}

/// A Python module implemented in Rust.
#[pymodule]
fn floatdb(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(generate_hash, m)?)?;
    Ok(())
}
