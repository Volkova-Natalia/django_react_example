import React, { Component } from "react";
import CustomersService from "./CustomersService";

const customersService = new CustomersService();

class CustomersList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            customers: [],
            countCustomers: 0,
            numPages:0,
            prevPageURL: '',
            nextPageURL: '',
        };
        this.prevPage = this.prevPage.bind(this);
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

    componentDidMount() {
        var self = this;
        customersService.getCustomers().then(function (result) {
            self._console_log_result(result);
            self._setState(result);
        });
    }

    handleDelete(e, pk){
        var self = this;
        customersService.deleteCustomer({pk: pk}).then(()=>{
            var newArr = self.state.customers.filter(function (obj) {
                return obj.pk !== pk;
            });

            self.setState({customer: newArr})
        });
    }
    prevPage(){
        var self = this;
        console.log(this.state.prevPageURL);
        customersService.getCustomersByURL(this.state.prevPageURL).then((result)=>{
            self._console_log_result(result);
            self._setState(result);
        });
    }
    nextPage(){
        var self = this;
        console.log(this.state.nextPageURL);
        customersService.getCustomersByURL(this.state.nextPageURL).then((result)=>{
            self._console_log_result(result);
            self._setState(result);
        });
    }

    _console_log_result(result){
        console.log("count = ", result.count_customers);
        console.log("num   = ", result.num_pages);
        console.log("prev  = ", result.prev_link);
        console.log("next  = ", result.next_link);
    }
    _setState(result){
        var self = this;
        self.setState({
            customers: result.data,
            countCustomers: result.count_customers,
            numPages: result.num_pages,
            prevPageURL: result.prev_link,
            nextPageURL: result.next_link,
        })
    }

    render() {
        return (
            <div className="customers--list">
                <table className="table">
                    <thead key="thead">
                    <tr>
                        <th>pk</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Address</th>
                        <th>Description</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.customers.map( c =>
                        <tr key={c.pk}>
                            <td>{c.pk}</td>
                            <td>{c.first_name}</td>
                            <td>{c.last_name}</td>
                            <td>{c.email}</td>
                            <td>{c.phone}</td>
                            <td>{c.address}</td>
                            <td>{c.description}</td>
                            <td>
                                <button onClick={(e)=> this.handleDelete(e, c.pk)}>Delete</button>
                                <a href={"/customer/" + c.pk}>Update</a>
                            </td>
                        </tr>
                    )}
                    </tbody>
                </table>
                <button className="btn btn-primary mr-2" onClick={ this.prevPage }>Prev</button>
                <button className="btn btn-primary mr-2" onClick={ this.nextPage }>Next</button>
            </div>
        );
    }
}
export default CustomersList;
