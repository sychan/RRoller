
package us.kbase.rroller;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: RRoll_Output</p>
 * <pre>
 * Here is the definition of the output of the function.  The output
 * can be used by other SDK modules which call your code, or the output
 * visualizations in the Narrative.  'report_name' and 'report_ref' are
 * special output fields- if defined, the Narrative can automatically
 * render your Report.
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report_name",
    "report_url"
})
public class RRollOutput {

    @JsonProperty("report_name")
    private String reportName;
    @JsonProperty("report_url")
    private String reportUrl;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report_name")
    public String getReportName() {
        return reportName;
    }

    @JsonProperty("report_name")
    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public RRollOutput withReportName(String reportName) {
        this.reportName = reportName;
        return this;
    }

    @JsonProperty("report_url")
    public String getReportUrl() {
        return reportUrl;
    }

    @JsonProperty("report_url")
    public void setReportUrl(String reportUrl) {
        this.reportUrl = reportUrl;
    }

    public RRollOutput withReportUrl(String reportUrl) {
        this.reportUrl = reportUrl;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((("RRollOutput"+" [reportName=")+ reportName)+", reportUrl=")+ reportUrl)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
