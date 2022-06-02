const mockedQuotas =  {
    "user1": Math.random(),
    "user2": Math.random(),
    "user3": Math.random(),
}

module.exports = {

    /**
     * Returns the ratio of service quota consumed by every user
     */
    all() {
        return mockedQuotas
    }

}